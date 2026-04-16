extends Node

const RUTA_SAVE = "user://save.json"

var habilitado = true

var datos: Dictionary = {
	"cuartoUma": {
		"luz": true,
	},
	"jugador": {
		"escena_actual": "res://scenes/world/CuartoUma.tscn",
		"posicion_x": 528,
		"posicion_y": 144,
		"ultima_direccion": "quietDown",
	},
	"ajustes": {
		"volumen_musica": 40.0,
		"volumen_sfx": 10.0,
		"tipo_control": "joystick",
	},
	"progreso": {
		"umbral_ocurrido": false,
		"clase_elegida": "",
		"senales_encontradas": [],
		"anclajes_activos": [],
		"npcs_conectados": {},
		"vaciados_liberados": [],
		"fragmentos_memoria": [],
		"muertes_uma": 0,
		"tiempo_jugado": 0.0,
	}
}

func _ready() -> void:
	cargar()
	_aplicar_ajustes()

func guardar() -> void:
	var archivo = FileAccess.open(RUTA_SAVE, FileAccess.WRITE)
	if archivo == null:
		print("Error al guardar")
		return
	archivo.store_string(JSON.stringify(datos, "\t"))
	archivo.close()
	print("Guardado OK")

func cargar() -> void:
	if not FileAccess.file_exists(RUTA_SAVE):
		print("No hay partida guardada — usando valores por defecto")
		return
	var archivo = FileAccess.open(RUTA_SAVE, FileAccess.READ)
	if archivo == null:
		return
	var resultado = JSON.parse_string(archivo.get_as_text())
	archivo.close()
	if resultado == null:
		print("Error al parsear save")
		return
	_merge(datos, resultado)
	print("Cargado OK")

func hay_partida() -> bool:
	return FileAccess.file_exists(RUTA_SAVE)

func borrar_partida() -> void:
	if FileAccess.file_exists(RUTA_SAVE):
		var err = DirAccess.remove_absolute(RUTA_SAVE)
		if err != OK:
			print("Error al borrar archivo: ", err)

	datos["progreso"] = {
		"umbral_ocurrido": false,
		"clase_elegida": "",
		"senales_encontradas": [],
		"anclajes_activos": [],
		"npcs_conectados": {},
		"vaciados_liberados": [],
		"fragmentos_memoria": [],
		"muertes_uma": 0,
		"tiempo_jugado": 0.0
	}

	print("Partida borrada")
	OS.create_process(OS.get_executable_path(), [])
	get_tree().quit()

func _merge(base: Dictionary, nuevo: Dictionary) -> void:
	for key in nuevo:
		if base.has(key):
			if base[key] is Dictionary and nuevo[key] is Dictionary:
				_merge(base[key], nuevo[key])
			else:
				base[key] = nuevo[key]

func _aplicar_ajustes() -> void:
	var bus_musica = AudioServer.get_bus_index("Musica")
	var bus_sfx    = AudioServer.get_bus_index("SFX")
	if bus_musica != -1:
		AudioServer.set_bus_volume_db(bus_musica, linear_to_db(datos["ajustes"]["volumen_musica"]))
	if bus_sfx != -1:
		AudioServer.set_bus_volume_db(bus_sfx, linear_to_db(datos["ajustes"]["volumen_sfx"]))

func get_ajuste(clave: String):
	return datos["ajustes"].get(clave)

func set_ajuste(clave: String, valor) -> void:
	datos["ajustes"][clave] = valor
	_aplicar_ajustes()
	guardar()

func get_jugador(clave: String):
	return datos["jugador"].get(clave)

func set_jugador(clave: String, valor) -> void:
	datos["jugador"][clave] = valor

func get_progreso(clave: String):
	return datos["progreso"].get(clave)

func set_progreso(clave: String, valor) -> void:
	datos["progreso"][clave] = valor
	
func set_cuarto(clave: String, valor) -> void:
	datos["cuartoUma"][clave] = valor
	
func get_cuarto(clave: String):
	return datos["cuartoUma"].get(clave)
