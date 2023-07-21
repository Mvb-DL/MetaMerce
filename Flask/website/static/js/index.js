
//delete the uploaded data
function deleteUpload(uploadId) {
  fetch("/delete-upload", {
    method: "POST",
    body: JSON.stringify({ uploadId: uploadId }),
  }).then((_res) => {
    window.location.href = "/home";
  });
}


//to delete the product data
function deleteProduct(ProductId){
  
  fetch(`${window.origin}/delete_product`, {
    method: "POST",
    body: JSON.stringify(ProductId),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  }).then((_res) => {
    window.location.href = "/company_profile";
  });

}


//to delete the company data
function deleteCompany(uploadId){

  fetch(`${window.origin}/delete_company`, {
    method: "POST",
    body: JSON.stringify(uploadId),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  }).then((_res) => {
    window.location.href = "/account";
  });

}



