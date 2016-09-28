function retLinkType(str) {
	var image_name = "";
	switch (str.toLowerCase()) {
		case "case":
			image_name = "case.jpg";
			break;
		case "controller":
			image_name = "controller.jpg";
			break;
		case "cooler":
			image_name = "cooler.jpg";
			break;
		case "cpu":
			image_name = "cpu.jpg";
			break;
		case "fan":
			image_name = "fan.jpg";
			break;
		case "fans":
			image_name = "fan.jpg";
			break;
		case "gpu":
			image_name = "gpu.jpg";
			break;
		case "graphics card":
			image_name = "gpu.jpg";
			break;
		case "hdd":
			image_name = "hdd.jpg";
			break;
		case "headphones":
			image_name = "headphones.jpg";
			break;
		case "keyboard":
			image_name = "keyboard.jpg";
			break;
		case "monitor":
			image_name = "monitor.jpg";
			break;
		case "mouse":
			image_name = "mouse.jpg";
			break;
		case "psu":
			image_name = "psu.jpg";
			break;
		case "ram":
			image_name = "ram.jpg";
			break;
		case "ssd":
			image_name = "ssd.jpg";
			break;
		case "mobo":
			image_name = "mobo.jpg";
			break;
		case "combo":
			image_name = "combo.jpg";
			break;
		case "racing wheel":
			image_name = "wheel.jpg";
			break;
		case "prebuilt":
			image_name = "prebuilt.jpg";
			break;
		case "barebones mini pc":
			image_name = "prebuilt.jpg";
			break;
		case "office chair":
			image_name = "chair.jpg";
			break;
		case "speakers":
			image_name = "speakers.jpg";
			break;
		case "mic":
			image_name = "mic.jpg";
			break;
		default:
			image_name = "no_icon.jpg";
			break;
	}
	return image_name;
}
