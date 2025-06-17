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

document.addEventListener("DOMContentLoaded", function () {
    // Модальное окно 1
    const modal1 = document.getElementById("myModal");
    const img1 = document.getElementById("myImg");
    const modalImg1 = document.getElementById("img01");
    const captionText1 = document.getElementById("caption");
    const span1 = document.getElementsByClassName("close")[0];

    if (img1 && modal1 && modalImg1 && captionText1) {
      img1.addEventListener("click", function () {
        modal1.style.display = "block";
        modalImg1.src = this.src;
        captionText1.textContent = this.alt;
      });
    }

    if (span1 && modal1) {
      span1.addEventListener("click", function () {
        modal1.style.display = "none";
      });
    }

    // Модальное окно 2
    const modal2 = document.getElementById("myModal1");
    const img2 = document.getElementById("myImg1");
    const modalImg2 = document.getElementById("img02");
    const captionText2 = document.getElementById("caption1");
    const span2 = document.getElementsByClassName("close1")[0];

    if (img2 && modal2 && modalImg2 && captionText2) {
      img2.addEventListener("click", function () {
        modal2.style.display = "block";
        modalImg2.src = this.src;
        captionText2.textContent = this.alt;
      });
    }

    if (span2 && modal2) {
      span2.addEventListener("click", function () {
        modal2.style.display = "none";
      });
    }

    // Модальное окно 3
    const modal3 = document.getElementById("myModal2");
    const img3 = document.getElementById("myImg2");
    const modalImg3 = document.getElementById("img03");
    const captionText3 = document.getElementById("caption2");
    const span3 = document.getElementsByClassName("close2")[0];

    if (img3 && modal3 && modalImg3 && captionText3) {
      img3.addEventListener("click", function () {
        modal3.style.display = "block";
        modalImg3.src = this.src;
        captionText3.textContent = this.alt;
      });
    }

    if (span3 && modal3) {
      span3.addEventListener("click", function () {
        modal3.style.display = "none";
      });
    }

    // Модальное окно 4
    const modal4 = document.getElementById("myModal3");
    const img4 = document.getElementById("myImg3");
    const modalImg4 = document.getElementById("img04");
    const captionText4 = document.getElementById("caption3");
    const span4 = document.getElementsByClassName("close3")[0];

    if (img4 && modal4 && modalImg4 && captionText4) {
      img4.addEventListener("click", function () {
        modal4.style.display = "block";
        modalImg4.src = this.src;
        captionText4.textContent = this.alt;
      });
    }

    if (span4 && modal4) {
      span4.addEventListener("click", function () {
        modal4.style.display = "none";
      });
    }
});

/* Чтобы сообщения исчезали через 15 сек */

// document.addEventListener("DOMContentLoaded", function () {
//   var messages = document.querySelectorAll(".messages li");
//   messages.forEach(function (message) {
//     setTimeout(function () {
//       message.style.display = "none";
//     }, 15000); // Сообщение исчезает через 15 секунд
//   });
// });

/* Подтверждение возроста*/
