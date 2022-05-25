(function () {
  window.$('DIV#add_item').click(function () {
    window.$('UL.my_list').append('<li>Item</li>');
  });

  window.$('DIV#remove_item').click(function () {
    const l = window.$('UL.my_list li');
    if (l.length > 0) { l[l.length - 1].remove(); }
  });
  window.$('DIV#clear_list').click(function () {
    const l = window.$('UL.my_list li');
    l.empty();
  });
})();
