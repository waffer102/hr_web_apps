new Sortable(toolBox, {
    group: {
        name: 'shared',
        pull: 'clone',
        put: false
    },
    sort: false,
    draggable: '.dragme'
});

Sortable.create(letterBox, {
    group: {
        name: 'shared'
    },
    store: {
        /**
         * Save the order of elements. Called onEnd (when the item is dropped).
         * @param {Sortable}  sortable
         */
        set: function (sortable) {
            var order = sortable.toArray();
            document.getElementById('letter_order[]').value = order;
            console.log(order);
        }
    },
    draggable: '.dragme',
    animation: 150,
    removeOnSpill: true,
    onAdd: function (evt) {
        var toolboxText = evt.item.querySelector(".toolboxText");
        var letterboxText = evt.item.querySelector(".letterboxText");
        toolboxText.style.display = "none";
        letterboxText.style.display = "block";
    }
})