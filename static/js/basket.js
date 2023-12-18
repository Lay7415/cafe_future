const btns = document.getElementsByClassName("quantity-buttons");
const total_amount = document.getElementById("total_amount");
const total_quantity = document.getElementById("total_quantity");
const delete_btns = document.getElementsByClassName("delete-btn");

for (let i = 0; i < btns.length; i++) {
  const element = btns[i];
  firstBtn = element.children[0];
  secondBtn = element.children[2];
  firstBtn.addEventListener("click", changeQuantity);
  secondBtn.addEventListener("click", changeQuantity);
}

for (let i = 0; i < delete_btns.length; i++) {
  const delete_btn = delete_btns[i];
  delete_btn.addEventListener('click', deleteFoodByFetch)
}

function changeQuantity(event) {
  event.stopPropagation();
  const foodId = event.target.dataset.foodId;
  const change = Number(event.target.dataset.change);
  const quantitySpan = document.querySelector(`#quantity-${foodId}`);
  const priceSpan = document.querySelector(`#price-${foodId}`);
  const currentQuantity = Number(quantitySpan.innerHTML);

  if (currentQuantity === 1 && change === -1) {
    return;
  }
  const newQuantity = currentQuantity + change;
  quantitySpan.innerHTML = newQuantity;
  const initalPrice = parseInt(priceSpan.innerHTML.split("$")[1]) / currentQuantity;
  const price = Number(newQuantity * initalPrice);
  priceSpan.innerHTML = `Price: $ ${price.toFixed(2)}`;
  total_amount.innerText = Number(total_amount.innerText) + change*initalPrice
  total_quantity.innerText = Number(total_quantity.innerText) + change
  return sendFoodByFetch(foodId, { quantity: newQuantity, price: price });
}

async function sendFoodByFetch(foodId, data) {
  const csrftoken = getCookie("csrftoken");

  const request = await fetch(
    `http://127.0.0.1:8000/client/basket/change/${foodId}/`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken, // Add the CSRF token to the headers
      },
      body: JSON.stringify(data),
    }
  );

  const res = await request.json();
}

async function deleteFoodByFetch(event) {
  const foodId = event.target.dataset.foodId;
  const quantitySpan = document.querySelector(`#quantity-${foodId}`);
  const priceSpan = document.querySelector(`#price-${foodId}`);
  const currentQuantity = Number(quantitySpan.innerHTML);
  const initalPrice = Number(priceSpan.innerHTML.split("$")[1]);
  total_amount.innerText = Number(total_amount.innerText) - initalPrice
  total_quantity.innerText = Number(total_quantity.innerText) - currentQuantity

  const request = await fetch(
    `http://127.0.0.1:8000/client/basket/delete/${foodId}/`
  );
  const res = request.json();
  event.target.parentNode.style.display = "none";
}



function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
