from flet import *


class CustomDataTable:
    def __init__(self, columns, data=None, on_item_selected=None):
        self.columns = [DataColumn(Text(col, color="#000000")) for col in columns]
        self.data = data or []
        self.on_item_selected = on_item_selected
        self.table = DataTable(columns=self.columns, rows=[])
        self.selected_index = None
        self._update_rows()

    def _update_rows(self):
        self.table.rows.clear()
        for i, row in enumerate(self.data):
            new_row = DataRow(
                cells=[DataCell(Text(str(cell), color="#000000")) for cell in row],
                color=Colors.RED_200 if self.selected_index == i else None,
                selected=(self.selected_index == i),
                on_select_changed=lambda e, index=i: self._select_item(index),
            )
            print(self.selected_index)
            self.table.rows.append(new_row)

    def _select_item(self, index):
        self.selected_index = index

        if self.on_item_selected:
            self.on_item_selected(self.data[index])
        self._update_rows()
        print(f"Selected index {self.selected_index}")
        self.table.update()

    def add_item(self, item):
        self.data.append(item)
        self._update_rows()

    def edit_item(self, index, updated_item):
        if 0 <= index < len(self.data):
            self.data[index] = updated_item
            self._update_rows()

    def delete_item(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
            self.selected_index = None
            self._update_rows()

    def load_data(self, new_data):
        self.data = new_data
        self._update_rows()

    def build(self):
        return self.table


class CustomDataTableEdit:
    def __init__(
        self,
        columns,
        data=None,
        on_item_selected=None,
        editable_columns=None,
        computed_column=None,
    ):
        """
        :param columns: Lista de nombres de columnas.
        :param data: Lista de datos de la tabla.
        :param on_item_selected: Callback al seleccionar una fila.
        :param editable_columns: Lista de índices de columnas editables.
        :param computed_column: Diccionario con:
            - name: Nombre de la columna calculada.
            - operation: Función para calcular el valor.
            - columns: Índices de las columnas involucradas en el cálculo.
        """
        self.columns = [DataColumn(Text(col, color="#000000")) for col in columns]
        self.column_names = columns  # Mantener los nombres originales de las columnas
        self.data = data or []
        self.on_item_selected = on_item_selected
        self.editable_columns = editable_columns or list(
            range(len(columns))
        )  # Todas las columnas son editables por defecto
        self.computed_column = computed_column  # Configuración de columna calculada
        if self.computed_column:
            self.columns.append(DataColumn(Text(self.computed_column["name"])))
            self.column_names.append(self.computed_column["name"])
            # Asegurarse de que cada fila tenga espacio para la columna calculada
            for row in self.data:
                if len(row) < len(self.column_names):
                    row.append(0)  # Inicializamos la columna calculada con 0
        self.table = DataTable(columns=self.columns, rows=[])
        self.selected_index = None
        self._update_rows()

    def _update_rows(self):
        self.table.rows.clear()
        for i, row in enumerate(self.data):
            cells = []
            # Crear celdas para las columnas regulares
            for col_index, cell in enumerate(row[: len(self.column_names) - 1]):
                if col_index in self.editable_columns:
                    cells.append(
                        DataCell(
                            TextField(
                                value=str(cell),
                                on_change=lambda e, index=i, col=col_index: self._update_cell(
                                    index, col, e.control.value
                                ),
                                border=InputBorder.NONE,
                            )
                        )
                    )
                else:
                    cells.append(DataCell(Text(str(cell), color="#000000")))

            # Calcular valor de la columna calculada (si existe)
            if self.computed_column:
                value = self._compute_column_value(row)
                cells.append(DataCell(Text(str(value), color="#000000")))
                row[len(self.column_names) - 1] = value  # Actualizar el dato en la fila

            new_row = DataRow(
                cells=cells,
                color=Colors.RED_200 if self.selected_index == i else None,
                selected=(self.selected_index == i),
                on_select_changed=lambda e, index=i: self._select_item(index),
            )
            self.table.rows.append(new_row)

    def _update_cell(self, row_index, col_index, new_value):
        try:
            # Actualizar el valor en la fila
            self.data[row_index][col_index] = float(
                new_value
            )  # Convertir a flotante para cálculos
            # Recalcular la fila si hay una columna calculada
            if self.computed_column and col_index in self.computed_column["columns"]:
                self.data[row_index][-1] = self._compute_column_value(
                    self.data[row_index]
                )
            self._update_rows()
            self.table.update()
        except ValueError:
            print(f"Valor inválido ingresado en la celda ({row_index}, {col_index}).")
        except IndexError:
            print("Error actualizando celda: índice fuera de rango.")

    def _select_item(self, index):
        self.selected_index = index
        if self.on_item_selected:
            self.on_item_selected(self.data[index])
        self._update_rows()
        self.table.update()

    def _compute_column_value(self, row):
        try:
            operation = self.computed_column["operation"]
            columns = self.computed_column["columns"]
            values = [float(row[col]) for col in columns]
            return operation(*values)
        except Exception as e:
            print(f"Error calculando valor: {e}")
            return "Error"

    def add_item(self, item):
        if self.computed_column:
            item.append(0)  # Inicializamos la columna calculada con 0
        self.data.append(item)
        self._update_rows()

    def edit_item(self, index, updated_item):
        if 0 <= index < len(self.data):
            self.data[index] = updated_item
            self._update_rows()

    def delete_item(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
            self.selected_index = None
            self._update_rows()

    def load_data(self, new_data):
        self.data = new_data
        # Asegurarse de que cada fila tenga espacio para la columna calculada
        if self.computed_column:
            for row in self.data:
                if len(row) < len(self.column_names):
                    row.append(0)  # Inicializamos la columna calculada con 0
        self._update_rows()

    def build(self):
        return self.table
