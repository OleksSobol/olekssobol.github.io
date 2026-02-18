(function() {
  var sequence = [
    'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
    'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight',
    'b', 'a'
  ];
  var position = 0;

  document.addEventListener('keydown', function(e) {
    if (e.key === sequence[position]) {
      position++;
      if (position === sequence.length) {
        window.location.href = '/lab/';
        position = 0;
      }
    } else {
      position = 0;
    }
  });
})();
