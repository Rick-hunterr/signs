extends Node2D

@onready var uma = $Uma

	
func _ready() -> void:
	uma.set_interactuables(DatosInteractuables.CUARTO_UMA)
	uma.set_sonidos_pasos(SonidosPasos.CUARTO_UMA)
	
