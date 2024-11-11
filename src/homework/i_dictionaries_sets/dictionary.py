#HW 8

def add_inventory(widgets, widget_name, quantity):
    widgets[widget_name]=quantity
    return widgets

def remove_inventory_widget(widgets, widget_name):
    if widget_name in widgets:
        del widgets[widget_name]
        return "Record deleted"
    else:
        return "Item not found"