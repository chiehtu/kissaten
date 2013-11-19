getCookie = (name) ->
    cookieValue = null

    if document.cookie and document.cookie isnt ''
        for cookie in (jQuery.trim(cookie) for cookie in document.cookie.split(';'))
            if cookie.substring(0, name.length + 1) is (name + '=')
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break

    return cookieValue

preview = document.createElement('div')

$('.btn.preview').click (e) ->
    e.preventDefault()
    self = $(this)
    target = $(self.data('target'))

    if self.hasClass('previewing')
        preview.remove()
        target.show()
        self.removeClass('previewing')
        return false

    self.addClass('previewing')
    content = target.val()
    csrftoken = getCookie('csrftoken')

    $.post '/markdown/', {content: content, csrfmiddlewaretoken: csrftoken}, (data) ->
        preview.innerHTML = data
        target.hide()
        target.after(preview)
        return

    $(preview).on 'click', ->
        preview.remove()
        target.show()
        return
    false
return