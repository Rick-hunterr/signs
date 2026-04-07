extends CanvasLayer

@onready var slider_musica = $Control/SliderMusica
@onready var slider_sfx    = $Control/SliderSFX
@onready var btn_joystick  = $Control/BtnJoystick
@onready var btn_gamepad   = $Control/BtnGamepad
@onready var btn_guardar   = $Control/BtnGuardar
@onready var btn_volver    = $Control/BtnVolver
@onready var modal = $Control/Modal

var desde_juego: bool = false

var player = null

func _ready() -> void:
	modal.visible = false
	
	process_mode = Node.PROCESS_MODE_ALWAYS
	hide()
	slider_musica.value = SaveManager.get_ajuste("volumen_musica")
	slider_sfx.value    = SaveManager.get_ajuste("volumen_sfx")
	_actualizar_botones_control()
	
	slider_musica.value_changed.connect(_on_slider_musica)
	slider_sfx.value_changed.connect(_on_slider_sfx)
	btn_joystick.pressed.connect(_on_btn_joystick)
	btn_gamepad.pressed.connect(_on_btn_gamepad)
	btn_guardar.pressed.connect(_on_btn_guardar)
	btn_volver.pressed.connect(_on_btn_volver)

func abrir(es_desde_juego: bool) -> void:
	desde_juego = es_desde_juego
	if desde_juego:
		get_tree().paused = true
	# Refrescar valores al abrir
	slider_musica.value = SaveManager.get_ajuste("volumen_musica")
	slider_sfx.value    = SaveManager.get_ajuste("volumen_sfx")
	_actualizar_botones_control()
	show()

func _on_slider_musica(valor: float) -> void:
	SaveManager.set_ajuste("volumen_musica", valor)

func _on_slider_sfx(valor: float) -> void:
	SaveManager.set_ajuste("volumen_sfx", valor)

func _on_btn_joystick() -> void:
	SaveManager.set_ajuste("tipo_control", "joystick")
	_actualizar_botones_control()
	_avisar_gui()

func _on_btn_gamepad() -> void:
	SaveManager.set_ajuste("tipo_control", "gamepad")
	_actualizar_botones_control()
	_avisar_gui()

func _on_btn_guardar() -> void:
	Ajustes.player.btnGuardar()
	SaveManager.guardar()
	print("Guardado desde ajustes")

func _on_btn_volver() -> void:
	SaveManager.guardar()
	if desde_juego:
		get_tree().paused = false
	hide()

func _avisar_gui() -> void:
	var gui = get_tree().get_first_node_in_group("gui")
	if gui:
		gui.actualizar_control()

func _actualizar_botones_control() -> void:
	var tipo = SaveManager.get_ajuste("tipo_control")
	btn_joystick.modulate = Color.WHITE if tipo == "joystick" else Color(0.5, 0.5, 0.5)
	btn_gamepad.modulate  = Color.WHITE if tipo == "gamepad"  else Color(0.5, 0.5, 0.5)

func _on_btn_salir_pressed() -> void:
	SaveManager.guardar()
	get_tree().paused = false
	Transition.play("res://scenes/ui/MainMenu.tscn", 0.1)
	hide()


func _on_btn_borrar_pressed() -> void:
	modal.visible = true


func _on_btn_si_pressed() -> void:
	modal.visible = false
	SaveManager.borrar_partida()


func _on_btn_no_pressed() -> void:
	modal.visible = false
	pass # Replace with function body.
