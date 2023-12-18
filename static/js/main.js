const btns = document.getElementsByClassName("new_products-btn");
const addedInBaskets = document.getElementsByClassName("added-in-basket");

for (const btn of btns) {
  btn.addEventListener("click", sendFoodByFetch);
}

for (const addedInBasket of addedInBaskets) {
  console.log(addedInBasket)
  addedInBasket.addEventListener("click", deleteFoodByFetch);
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

async function deleteFoodByFetch(event) {
  console.log('delete')
  const foodId = event.target.dataset.foodId;
  console.log(foodId)
  const request = await fetch(
    `http://127.0.0.1:8000/client/basket/basket_food/delete/${foodId}`
    );
    const res = request.json();
    console.log(res)
  event.target.style.display = "none";
  document.querySelector(`.new_products-btn-${foodId}`).style.display = "block";
}
