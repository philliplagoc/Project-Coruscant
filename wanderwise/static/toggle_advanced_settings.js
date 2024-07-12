document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("toggle").addEventListener("change", function() {
        var knows_date = document.getElementById("knows_date");
        var knows_duration = document.getElementById("knows_duration");

        if (this.checked) {  // User can select a calendar range.
            knows_date.style.display = 'block';
            knows_duration.style.display = 'none';
        } else {  // User doesn't know dates, so can choose a duration.
            knows_date.style.display = 'none';
            knows_duration.style.display = 'block';
        }
    });
});