function setScreenshotUrl(url) {

  document.getElementById('target').src = url;

  var product_image = document.createElement("a");
  product_image.href = url;
  product_image.download = "product_image.png";
  product_image.click();
}




