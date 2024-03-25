window.addEventListener('scroll', () => {
    const header = document.querySelector(".myheader");
    const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    
    if (scrollTop > 50) {
        header.style.backgroundColor = "rgba(37, 28, 17, 0.5)";
        header.style.height = "70px";
        header.style.padding = "10px 0";
    } else {
        header.style.backgroundColor = "rgba(37, 28, 17, 1)";
        header.style.height = "100px";
        header.style.padding = "20px 0";
    }
});

let typingFlag = false;

document.querySelectorAll('.contact-input').forEach(input => {
    input.addEventListener('input', () => {
        typingFlag = true;
    });

    input.addEventListener('focus', () => {
        if (!typingFlag) {
            input.style.transform = 'scale(1.1)';
        }
    });

    input.addEventListener('blur', () => {
        typingFlag = false;
        input.style.transform = 'scale(1)';
    });
});

document.querySelector('.contact-input').addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        typingFlag = false;
    }
});





