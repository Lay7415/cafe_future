const btns = document.getElementsByClassName("new_products-btn");

for (const btn of btns) {
  btn.addEventListener("click", sendFoodByFetch);
}

async function sendFoodByFetch(event) {
  const foodId = event.target.dataset.foodId;
  console.log(foodId);
  const request = await fetch(
    `http://127.0.0.1:8000/client/basket/create/${foodId}`
  );
  const res = request.json();
  console.dir(event.target);
  event.target.style.display = "none";
  document.querySelector(`.added-in-basket-${foodId}`).style.display = "block";
}
