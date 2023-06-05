'use strict';

function scrollToNarrative(index) {
  var narrativeId = 'narrative-' + index;
  var narrativeElement = document.getElementById(narrativeId);
  if (narrativeElement) {
    narrativeElement.scrollIntoView({ behavior: 'smooth' });
  }
}
