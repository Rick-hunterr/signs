extends CharacterBody2D

var joystick : Joystick = null

@onready var Uma = $AnimatedSprite2D
@onready var ray = $RayCast2D
@onready var ray_interact = $RayCast2DInteracts
@onready var camera = $Camera2D
@onready var audio_pasos = $AudioPasos

var en_dialogo: bool = false

var dialogoCuartoUma = preload("res://scripts/dialogue/cuartoUma.dialogue")

var camera_pos: Vector2 = Vector2.ZERO
const CAMERA_SPEED: float = 5.0

var gamepad_hold_time: float = 0.0
var gamepad_holding: bool = false
const GAMEPAD_HOLD_THRESHOLD: float = 0.15

var direccion_gamepad: Vector2 = Vector2.ZERO
var SONIDOS_PASOS: Dictionary = {}

const TILE_SIZE = 32
const SPEED = 100.0
var speed_actual: float = SPEED

var moving = false
var target_position: Vector2
var direction = Vector2.ZERO
var lastDirection = "quietDown"
var bump_offset: Vector2 = Vector2.ZERO


var tilemap_objetos : TileMapLayer = null
var TILES_INTERACTUABLES: Dictionary = {}



func set_interactuables(datos: Dictionary) -> void:
	TILES_INTERACTUABLES = datos

func _ready():
	camera.position_smoothing_enabled = false

	Ajustes.player = self
	_aplicar_posicion_guardada()

	camera_pos = global_position

	# Forzar la cámara a la posición correcta ANTES del await
	camera.position = Vector2.ZERO
	camera.global_position = global_position

	target_position = position
	update_raycast()

	await get_tree().process_frame

	# Después del await confirmar los límites
	set_camera_limits()
	tilemap_objetos = _buscar_tilemap("Objetos")

	var gui = get_tree().get_first_node_in_group("gui")
	if gui:
		gui.boton_interactuar_presionado.connect(_on_interactuar)
		gui.boton_direccion_presionado.connect(_on_direccion_presionada)
		gui.boton_direccion_soltado.connect(_on_direccion_soltada)

func _aplicar_posicion_guardada() -> void:
	var escena_guardada = SaveManager.get_jugador("escena_actual")
	var escena_nivel = get_parent().scene_file_path
	if escena_nivel == "":
		escena_nivel = get_tree().current_scene.scene_file_path
	if escena_guardada != escena_nivel:
		return
	var pos_x = SaveManager.get_jugador("posicion_x")
	var pos_y = SaveManager.get_jugador("posicion_y")
	var ultima_dir = SaveManager.get_jugador("ultima_direccion")
	if pos_x != null and pos_y != null and (pos_x != 0 or pos_y != 0):
		position = Vector2(pos_x, pos_y)
		lastDirection = ultima_dir
		print("Posición aplicada: ", position)

func _on_direccion_presionada(dir: Vector2) -> void:
	direccion_gamepad = dir
	gamepad_hold_time = 0.0
	gamepad_holding = false
	match dir:
		Vector2.DOWN:  set_direction_sin_mover(Vector2.DOWN, "down", "quietDown")
		Vector2.UP:    set_direction_sin_mover(Vector2.UP, "up", "quietUp")
		Vector2.LEFT:  set_direction_sin_mover(Vector2.LEFT, "left", "quietLeft")
		Vector2.RIGHT: set_direction_sin_mover(Vector2.RIGHT, "right", "quietRight")

func _on_direccion_soltada() -> void:
	direccion_gamepad = Vector2.ZERO
	gamepad_holding = false
	gamepad_hold_time = 0.0

func set_sonidos_pasos(datos: Dictionary) -> void:
	SONIDOS_PASOS = datos
	if SONIDOS_PASOS.has("pasos"):
		audio_pasos.stream = load(SONIDOS_PASOS["pasos"])

func _buscar_tilemap(nombre: String) -> TileMapLayer:
	for node in get_tree().get_nodes_in_group("tilemaps"):
		if node.name == nombre:
			return node
	return _buscar_tilemap_recursivo(get_parent(), nombre)

func _buscar_tilemap_recursivo(node: Node, nombre: String) -> TileMapLayer:
	for child in node.get_children():
		if child is TileMapLayer and child.name == nombre:
			return child
		if child.get_child_count() > 0:
			var resultado = _buscar_tilemap_recursivo(child, nombre)
			if resultado:
				return resultado
	return null

func recibir_joystick(j: Joystick):
	joystick = j

func _physics_process(delta):
	camera_pos = camera_pos.lerp(global_position, CAMERA_SPEED * delta)
	camera.global_position = camera_pos.round()

	if direccion_gamepad != Vector2.ZERO and not gamepad_holding:
		gamepad_hold_time += delta
		if gamepad_hold_time >= GAMEPAD_HOLD_THRESHOLD:
			gamepad_holding = true

	if bump_offset != Vector2.ZERO:
		bump_offset = bump_offset.lerp(Vector2.ZERO, 0.3)
		if bump_offset.length() < 0.5:
			bump_offset = Vector2.ZERO
		Uma.position = bump_offset
		
	if en_dialogo:
		velocity = Vector2.ZERO # no moverse
		return # no procesar input
	if moving:
		move_to_target(delta)
	else:
		handle_input()
func _input(event):
	if event.is_action_pressed("interact"):
		_on_interactuar()

func handle_input():
	direction = Vector2.ZERO
	var tipo_control = SaveManager.get_ajuste("tipo_control")

	if tipo_control == "joystick" and joystick != null and joystick.index != -1:
		var dir = joystick.direccion
		var distancia = joystick.distancia
		var factor = clamp(distancia / joystick.radio, 0.0, 1.0)
		speed_actual = lerp(80.0, 120.0, factor)
		if abs(dir.x) > abs(dir.y):
			if dir.x > 0.15:
				set_direction_sin_mover(Vector2.RIGHT, "right", "quietRight")
				if distancia > joystick.radio * 0.6:
					set_direction(Vector2.RIGHT, "right", "quietRight")
			elif dir.x < -0.15:
				set_direction_sin_mover(Vector2.LEFT, "left", "quietLeft")
				if distancia > joystick.radio * 0.6:
					set_direction(Vector2.LEFT, "left", "quietLeft")
		else:
			if dir.y > 0.15:
				set_direction_sin_mover(Vector2.DOWN, "down", "quietDown")
				if distancia > joystick.radio * 0.6:
					set_direction(Vector2.DOWN, "down", "quietDown")
			elif dir.y < -0.15:
				set_direction_sin_mover(Vector2.UP, "up", "quietUp")
				if distancia > joystick.radio * 0.6:
					set_direction(Vector2.UP, "up", "quietUp")

	elif tipo_control == "gamepad" and direccion_gamepad != Vector2.ZERO:
		speed_actual = SPEED
		if gamepad_holding:
			if direccion_gamepad == Vector2.DOWN:
				set_direction(Vector2.DOWN, "down", "quietDown")
			elif direccion_gamepad == Vector2.UP:
				set_direction(Vector2.UP, "up", "quietUp")
			elif direccion_gamepad == Vector2.LEFT:
				set_direction(Vector2.LEFT, "left", "quietLeft")
			elif direccion_gamepad == Vector2.RIGHT:
				set_direction(Vector2.RIGHT, "right", "quietRight")
		else:
			quietAnimation()
	else:
		speed_actual = SPEED
		if Input.is_action_pressed("moveDown"):
			set_direction(Vector2.DOWN, "down", "quietDown")
		elif Input.is_action_pressed("moveUp"):
			set_direction(Vector2.UP, "up", "quietUp")
		elif Input.is_action_pressed("moveLeft"):
			set_direction(Vector2.LEFT, "left", "quietLeft")
		elif Input.is_action_pressed("moveRight"):
			set_direction(Vector2.RIGHT, "right", "quietRight")

	if direction != Vector2.ZERO:
		start_move()
	else:
		quietAnimation()

func set_direction_sin_mover(dir, anim, idle_anim) -> void:
	Uma.play(anim)
	lastDirection = idle_anim
	var ray_dir = dir * TILE_SIZE
	ray.target_position = ray_dir
	ray_interact.target_position = ray_dir

func set_direction(dir, anim, idle_anim):
	direction = dir
	Uma.play(anim)
	lastDirection = idle_anim
	update_raycast()

func start_move():
	if audio_pasos.stream != null:
		pass
		audio_pasos.play()
	update_raycast()
	ray.force_raycast_update()
	if ray.is_colliding():
		bump_offset = direction * 6
		return
	moving = true
	target_position = position + direction * TILE_SIZE

func move_to_target(_delta):
	var diff = target_position - position
	var step = speed_actual * _delta

	if diff.length() <= step:
		position = target_position
		moving = false
		velocity = Vector2.ZERO
		Uma.position = Vector2.ZERO
		quietAnimation()
		_detectar_tile_actual()
	else:
		# Mover directo por position, redondeado a entero para evitar subpíxeles
		position += diff.normalized() * step
		position = position.round()

func _detectar_tile_actual() -> void:
	if tilemap_objetos == null:
		return
	var tile_coords = tilemap_objetos.local_to_map(tilemap_objetos.to_local(position))
	var atlas_coords = tilemap_objetos.get_cell_atlas_coords(tile_coords)
	if atlas_coords == Vector2i(-1, -1):
		return
	if atlas_coords in TILES_INTERACTUABLES:
		var datos = TILES_INTERACTUABLES[atlas_coords]
		if datos["tipo"] == "puerta":
			guardar_posicion(datos["destino"])
			Transition.play(datos["destino"])

func quietAnimation():
	Uma.play(lastDirection)

func update_raycast():
	if direction == Vector2.DOWN:
		ray.target_position = Vector2(0, TILE_SIZE)
		ray_interact.target_position = Vector2(0, TILE_SIZE)
	elif direction == Vector2.UP:
		ray.target_position = Vector2(0, -TILE_SIZE)
		ray_interact.target_position = Vector2(0, -TILE_SIZE)
	elif direction == Vector2.LEFT:
		ray.target_position = Vector2(-TILE_SIZE, 0)
		ray_interact.target_position = Vector2(-TILE_SIZE, 0)
	elif direction == Vector2.RIGHT:
		ray.target_position = Vector2(TILE_SIZE, 0)
		ray_interact.target_position = Vector2(TILE_SIZE, 0)

func set_camera_limits():
	var min_pos = Vector2(INF, INF)
	var max_pos = Vector2(-INF, -INF)
	var found = false
	var tilemaps = get_tree().get_nodes_in_group("tilemaps")
	if tilemaps.is_empty():
		tilemaps = _find_tilemaps(get_parent())
	for node in tilemaps:
		var rect = node.get_used_rect()
		var top_left  = node.to_global(node.map_to_local(rect.position))
		var bot_right = node.to_global(node.map_to_local(rect.position + rect.size))
		min_pos.x = min(min_pos.x, top_left.x)
		min_pos.y = min(min_pos.y, top_left.y)
		max_pos.x = max(max_pos.x, bot_right.x)
		max_pos.y = max(max_pos.y, bot_right.y)
		found = true
	if not found:
		print("No se encontraron TileMapLayer")
		return
	camera.limit_left   = int(min_pos.x)
	camera.limit_top    = int(min_pos.y)
	camera.limit_right  = int(max_pos.x)
	camera.limit_bottom = int(max_pos.y)

func _find_tilemaps(node: Node) -> Array:
	var result = []
	for child in node.get_children():
		if child is TileMapLayer:
			result.append(child)
		if child.get_child_count() > 0:
			result.append_array(_find_tilemaps(child))
	return result

func guardar_posicion(escena_destino: String) -> void:
	print("Guardando posición: ", position)
	SaveManager.set_jugador("escena_actual", escena_destino)
	SaveManager.set_jugador("posicion_x", position.x)
	SaveManager.set_jugador("posicion_y", position.y)
	SaveManager.set_jugador("ultima_direccion", lastDirection)
	SaveManager.guardar()
	print("Datos guardados: ", SaveManager.datos["jugador"])

func resetear_control() -> void:
	direccion_gamepad = Vector2.ZERO
	gamepad_holding = false
	gamepad_hold_time = 0.0
	direction = Vector2.ZERO

func _on_interactuar() -> void:
	ray_interact.force_raycast_update()
	if ray_interact.is_colliding():
		var obj = ray_interact.get_collider()
		if obj and obj.has_method("interact"):
			obj.interact()
		return
	if tilemap_objetos == null:
		return
	var dir_actual = direction
	if dir_actual == Vector2.ZERO:
		match lastDirection:
			"quietDown":  dir_actual = Vector2.DOWN
			"quietUp":    dir_actual = Vector2.UP
			"quietLeft":  dir_actual = Vector2.LEFT
			"quietRight": dir_actual = Vector2.RIGHT
	var tile_pos = tilemap_objetos.local_to_map(
		tilemap_objetos.to_local(position + dir_actual * TILE_SIZE)
	)
	var atlas_coords = tilemap_objetos.get_cell_atlas_coords(tile_pos)
	if atlas_coords == Vector2i(-1, -1):
		return
	if atlas_coords in TILES_INTERACTUABLES:
		var datos = TILES_INTERACTUABLES[atlas_coords]
		match datos["tipo"]:
			"dialogo":
				en_dialogo = true
				DialogueManager.show_dialogue_balloon(dialogoCuartoUma, 'startCama')
				await DialogueManager.dialogue_ended
				en_dialogo = false
			"mesaCuartoUma":
				en_dialogo = true
				DialogueManager.show_dialogue_balloon(dialogoCuartoUma, 'startMesa')
				await DialogueManager.dialogue_ended
				en_dialogo = false
			"perchero":
				en_dialogo = true
				DialogueManager.show_dialogue_balloon(dialogoCuartoUma, 'startPerchero')
				await DialogueManager.dialogue_ended
				en_dialogo = false
			"armario":
				en_dialogo = true
				DialogueManager.show_dialogue_balloon(dialogoCuartoUma, 'startArmario')
				await DialogueManager.dialogue_ended
				en_dialogo = false
			"espejo":
				en_dialogo = true
				DialogueManager.show_dialogue_balloon(dialogoCuartoUma, 'startEspejo')
				await DialogueManager.dialogue_ended
				en_dialogo = false
			"objetos":
				en_dialogo = true
				DialogueManager.show_dialogue_balloon(dialogoCuartoUma, 'startObjetos')
				await DialogueManager.dialogue_ended
				en_dialogo = false
				
				
			"puerta":
				guardar_posicion(datos["destino"])
				Transition.play(datos["destino"])
			"señal":
				print("Señal: ", datos["id"])
			"item":
				print("Item: ", datos["id"])
	else:
		print("Atlas coords: ", atlas_coords)

func cargar_posicion() -> void:
	var escena_guardada = SaveManager.get_jugador("escena_actual")
	var escena_actual = get_tree().current_scene.scene_file_path
	print("Escena guardada: ", escena_guardada)
	print("Escena actual: ", escena_actual)
	if escena_guardada != escena_actual:
		return
	var pos_x = SaveManager.get_jugador("posicion_x")
	var pos_y = SaveManager.get_jugador("posicion_y")
	var ultima_dir = SaveManager.get_jugador("ultima_direccion")
	if pos_x != null and pos_y != null:
		position = Vector2(pos_x, pos_y)
		target_position = position
		lastDirection = ultima_dir
		print("Posición cargada: ", position)

func btnGuardar() -> void:
	var escena_actual = get_tree().current_scene.scene_file_path
	guardar_posicion(escena_actual)
	print("guardada")
