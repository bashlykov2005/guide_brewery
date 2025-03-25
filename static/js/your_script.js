// let t = document.getElementById("cursor");
// document.querySelector(".section-row").addEventListener("mousemove", function(n) {
//       t.style.left = n.clientX + "px",
//       t.style.top = n.clientY + "px"
//   });
//   function n() {
//         t.classList.add("hover")
//     }
//     function s() {
//           t.classList.remove("hover")
//       }
//       function o(t) {
//             t.addEventListener("mouseover", n), t.addEventListener("mouseout", s)
//         }
// document.addEventListener('DOMContentLoaded', function () {
//   let hoverLink = document.querySelectorAll(".hover-img");
//   for (let i = 0; i < hoverLink.length; i++) {
//     o(hoverLink[i]);
//     let url = hoverLink[i].getAttribute("data-url");
//     hoverLink[i].addEventListener('mouseenter', function () {
//       t.style.backgroundImage = "url(" + url + ")";
//     });
//   }
// });

  document.addEventListener("DOMContentLoaded", function (event) {
    var modal = document.getElementById('myModal');

    // Get the image and insert it inside the modal - use its "alt" text as a caption
    var img = document.getElementById('myImg');
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");
    img.onclick = function () {
      modal.style.display = "block";
      modalImg.src = this.src;
      captionText.innerHTML = this.alt;
    }

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
      modal.style.display = "none";
    }
  });


  document.addEventListener("DOMContentLoaded", function (event) {
    var modal = document.getElementById('myModal1');

  // Get the image and insert it inside the modal - use its "alt" text as a caption
  var img = document.getElementById('myImg1');
  var modalImg = document.getElementById("img02");
  var captionText = document.getElementById("caption1");
  img.onclick = function () {
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
  }

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close1")[0];

  // When the user clicks on <span> (x), close the modal
  span.onclick = function () {
    modal.style.display = "none";
  }
});


document.addEventListener("DOMContentLoaded", function (event) {
  var modal = document.getElementById('myModal2');

  // Get the image and insert it inside the modal - use its "alt" text as a caption
  var img = document.getElementById('myImg2');
  var modalImg = document.getElementById("img03");
  var captionText = document.getElementById("caption2");
  img.onclick = function () {
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
  }

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close2")[0];

  // When the user clicks on <span> (x), close the modal
  span.onclick = function () {
    modal.style.display = "none";
  }
});

document.addEventListener("DOMContentLoaded", function (event) {
  var modal = document.getElementById('myModal3');

  // Get the image and insert it inside the modal - use its "alt" text as a caption
  var img = document.getElementById('myImg3');
  var modalImg = document.getElementById("img04");
  var captionText = document.getElementById("caption3");
  img.onclick = function () {
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
  }

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close3")[0];

  // When the user clicks on <span> (x), close the modal
  span.onclick = function () {
    modal.style.display = "none";
  }
});
