extends Area2D

class_name Joystick

# VARIABLES PRINCIPALES
var distancia: float = 0.0
var direccion: Vector2 = Vector2.ZERO
var index: int = -1

# REFERENCIAS A NODOS
@onready var circulo = $circulo
@onready var punto = $punto
@onready var radio = $CollisionShape2D.shape.radius

func _ready():
	# Asegurar que el punto arranca en el centro
	punto.position = Vector2.ZERO

func _input(event: InputEvent) -> void:
	# DETECCIÓN DE TOQUE
	if event is InputEventScreenTouch:
		if event.is_pressed() and index == -1:
			if global_position.distance_to(event.position) < radio:
				index = event.index
				punto.modulate = Color("ffffffe1")
		elif not event.is_pressed() and event.index == index:
			index = -1
			distancia = 0.0
			direccion = Vector2.ZERO
			punto.modulate = Color("bcbcbcb3")

	# DETECCIÓN DE ARRASTRE
	if event is InputEventScreenDrag:
		if event.index == index:
			var local_pos = to_local(event.position)
			distancia = local_pos.length()

			if distancia <= radio:
				punto.position = local_pos
			else:
				punto.position = local_pos.normalized() * radio

			direccion = punto.position.normalized()

func _process(delta):
	# RETORNO SUAVE AL CENTRO
		
	if index == -1:
		punto.position = punto.position.lerp(Vector2.ZERO, 10 * delta)
