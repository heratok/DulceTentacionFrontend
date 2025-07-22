from flet import *

from app.components.billing.bill_list_item import BillListItem


class BillListView(Container):
    def __init__(self, items, page=Page):
        super().__init__()
        # self.inventoryInstance = Inventory()
        self.page = page
        self.items = items
        self.shadow_color = Colors.RED_300
        # self.item_select = ItemViewSelect(data={}, page=self.page,)
        self.item_select_data = None
        self.listItemsWidget = []
        self.loadItemWidget(self.items)
        self.content = Container(
            padding=0,
            expand=1,
            content=Column(
                expand=1,
                scroll=ScrollMode.ALWAYS,
                controls=self.listItemsWidget,
            ),
        )

    def loadItemWidget(self, list):
        self.listItemsWidget = [
            BillListItem(
                item,
                self.page,
                on_select=lambda e, item=item: self.select_item(item),
                index=index,
            ).build()
            for index, item in enumerate(list)
        ]

    def select_item(self, data):
        self.item_select_data = data
        # self.item_select.set_data(data)

    def build(self):
        return self.content
