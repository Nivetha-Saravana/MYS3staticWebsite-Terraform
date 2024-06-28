document.addEventListener('DOMContentLoaded', function () {
    const typingText = document.querySelector('.typing-text');
    const phrases = ['a Developer', 'a Designer', 'a Student'];
    let phraseIndex = 0;
    let letterIndex = 0;
    let currentPhrase = '';
    let isDeleting = false;

    function type() {
        if (letterIndex < phrases[phraseIndex].length && !isDeleting) {
            currentPhrase += phrases[phraseIndex].charAt(letterIndex);
            letterIndex++;
        } else {
            isDeleting = true;
            if (letterIndex > 0) {
                currentPhrase = currentPhrase.slice(0, -1);
                letterIndex--;
            } else {
                isDeleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
            }
        }

        typingText.textContent = currentPhrase;
        setTimeout(type, isDeleting ? 100 : 200);
    }

    type();
});
