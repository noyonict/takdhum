;(function ($) {
  $(window).load(function () {
    var accHeight = $('#accordion').height()
    var vw = $(window).width()
    $('#videoDisplay').css(
      'min-height',
      Math.min(vw < 640 ? 0 : vw, accHeight)
    )

    $('#accordion .list-video').each(function () {
      var self = $(this)
      if (!self.data('link')) return
      self.on('click', function () {
        var self = $(this)
        $('#videoDisplay').html(
          '<div class="embed-responsive embed-responsive-16by9">' +
            '<iframe class="embed-responsive-item "allowfullscreen src="' +
            self.data('link') +
            '"></iframe>' +
            '</div>'
        )
      })
    })
  })
})(window.jQuery)
