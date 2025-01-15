$(document).ready(function() {
    // Handle interest buttons
    $('.interest-btn').click(function() {
        const button = $(this);
        const ideaId = button.data('id');
        const action = button.data('action');

        $.ajax({
            url: `/ideas/${ideaId}/interest/`,
            method: 'POST',
            data: {
                action: action,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                button.closest('.idea-item').find('p:contains("Interest")').text(`Interest: ${response.interest}`);
            },
            error: function() {
                alert('Error updating interest');
            }
        });
    });

    // Handle star buttons
    $('.star-btn').click(function() {
        const button = $(this);
        const ideaId = button.data('id');

        $.ajax({
            url: `/ideas/${ideaId}/star/`,
            method: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                if (response.is_starred) {
                    button.text('⭐');
                } else {
                    button.text('☆');
                }
            },
            error: function() {
                alert('Error toggling star');
            }
        });
    });
});