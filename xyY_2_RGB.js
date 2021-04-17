function xyy2xyz (x, y, yy) {
	if (y == 0) return [0,0,0];
	return [
		normalize((x*yy)/y),
		normalize(yy),
		normalize(((1-x-y)*yy)/y)
	];
}

function cdm22yy (cdm2) {
	return normalize(cdm2/92.46);
}

function load (x,y,yy) {
	document.getElementById('x').value = x;
	document.getElementById('y').value = y;
	document.getElementById('yy').value = yy;
	init();
}

function xyz2rgb (x, y, z) {
	// http://www.brucelindbloom.com/index.html?Eqn_xyY_to_XYZ.html
	// CIE RGB [M]^-1
	var gamma = 1/2.2;
	var r = Math.max((2.3706743*x)+(-0.9000405*y)+(-0.4706338*z),0);
	var g = Math.max((-0.5138850*x)+(1.4253036*y)+(0.0885814*z),0);
	var b = Math.max((0.0052982*x)+(-0.0146949*y)+(1.0093968*z),0);
	return [Math.pow(r,gamma),Math.pow(g,gamma),Math.pow(b,gamma)];
}

function xyy2rgb (x, y, yy) {
	var xyz = xyy2xyz(x,y,yy);
	var e = document.getElementById('rgb');
	e.innerHTML = "XYZ: "+xyz+"<br />";
	return xyz2rgb.apply(this, xyz);
}

function init () {
	var x = document.getElementById('x').value;
	var y = document.getElementById('y').value;
	var yy = cdm22yy(document.getElementById('yy').value);
	var rgb = xyy2rgb(x,y,yy);
	var e = document.getElementById('rgb');
	e.innerHTML += "RGB: "+rgb+"<br />";
	rgb[0] = normalize(rgb[0]);
	rgb[1] = normalize(rgb[1]);
	rgb[2] = normalize(rgb[2]);

	var r255 = Math.round(rgb[0]*255);
	var g255 = Math.round(rgb[1]*255);
	var b255 = Math.round(rgb[2]*255);
	e.innerHTML += "RGB: "+[r255,g255,b255]+"<br />";
	var rhex = dec2hex(r255);
	var ghex = dec2hex(g255);
	var bhex = dec2hex(b255);
	var color = ""+rhex+""+ghex+""+bhex;
	e.innerHTML += "#"+color;
	e.style.backgroundColor = '#'+color;
}

function normalize (n) {
	return Math.max(0,Math.min(n,1));
}

function dec2hex(d) {
	var padding = 2;
    var hex = Number(d).toString(16);
    padding = typeof (padding) === "undefined" || padding === null ? padding = 2 : padding;

    while (hex.length < padding) {
        hex = "0" + hex;
    }

    return hex;
}
