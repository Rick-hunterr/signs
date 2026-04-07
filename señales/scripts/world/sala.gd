extends Node2D

@onready var uma = $Uma

func _ready() -> void:
	uma.set_interactuables(DatosInteractuables.CUARTO_UMA)
	uma.set_sonidos_pasos(SonidosPasos.CUARTO_UMA)
	await get_tree().process_frame
	await get_tree().process_frame
	uma.cargar_posicion()
