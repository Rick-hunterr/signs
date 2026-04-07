extends CanvasLayer

signal transition_finished  ## Emitida al completar play()

@onready var color_rect: ColorRect = $ColorRect

func _ready() -> void:
	color_rect.modulate.a = 0.0
	color_rect.mouse_filter = Control.MOUSE_FILTER_IGNORE

func play(target_scene: String, duration: float = 0.4) -> void:
	print("Transition.play() llamado → ", target_scene)
	color_rect.mouse_filter = Control.MOUSE_FILTER_STOP
	await _fade(1.0, duration)
	print("fade out terminado, cambiando escena")
	get_tree().change_scene_to_file(target_scene)
	await _fade(0.0, duration)
	print("fade in terminado")
	color_rect.mouse_filter = Control.MOUSE_FILTER_IGNORE
	transition_finished.emit()

func fade_out(duration: float = 0.4) -> void: 
	color_rect.mouse_filter = Control.MOUSE_FILTER_STOP
	await _fade(1.0, duration)

func fade_in(duration: float = 0.4) -> void:
	await _fade(0.0, duration)
	color_rect.mouse_filter = Control.MOUSE_FILTER_IGNORE

func _fade(target_alpha: float, duration: float) -> void:
	var tween = create_tween()
	tween.tween_property(color_rect, "modulate:a", target_alpha, duration)
	await tween.finished
