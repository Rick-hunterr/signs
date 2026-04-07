extends ParallaxBackground

@export var velocidad := 40.0
var scroll_value := 0.0
func _process(delta):
	scroll_value += velocidad * delta
	scroll_offset.x = int(scroll_value)
