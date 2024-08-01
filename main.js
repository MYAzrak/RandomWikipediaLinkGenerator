document.getElementById("randomButton").addEventListener("click", () => {
  fetch("http://127.0.0.1:5000/random-wikipedia-link")
    .then((response) => response.json())
    .then((data) => {
      window.location.href = data.url;
    })
    .catch((error) => console.error("Error:", error));
});
