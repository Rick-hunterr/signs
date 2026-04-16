extends Node2D

@onready var uma = $Uma
@onready var luz1 = $luz1
@onready var luz2 = $luz2

	
func _ready() -> void:
	uma.set_interactuables(DatosInteractuables.CUARTO_UMA)
	uma.set_sonidos_pasos(SonidosPasos.CUARTO_UMA)
	uma.recibirNodo(luz1, luz2)
	
