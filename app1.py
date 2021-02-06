import streamlit as st

# PPTX Page -------------------------------
def app():
    st.title('PPTX Code Reference')
    st.write('Sample PPTX Code')

    option = st.selectbox(
    "What code would you like to reference?", ("Graphs", "Functions", "Tables"))

    st.write("You selected:", option)

    if option == "Graphs":
        # Bar Chart #1
        st.subheader('Bar Chart #1')

        bar_chart_one = """
# define chart using find_shape_by_name function
chart = find_shape_by_name(SLIDE_NAME.shapes, 'chart_object_name')

def generate_bar_graph(chart):
    # define chart data
    chart_data = CategoryChartData()
    # define category names
    chart_data.categories = ['Jan 29', 'Jan 30']
    # change data
    chart_data.add_series('Negative', (100, 40))
    chart_data.add_series('Positive', (100, 40))
    chart_data.add_series('Neutral', (100, 40))

    chart.chart.replace_data(chart_data)
    """
        st.code(bar_chart_one, language='python')

    if option == "Functions":
        # PP Shape Objects #1
        st.subheader('Find Object Shapes on PowerPoint #1')

        code_shapes = """
# define find shape by ID function
def find_shape_by_id(shapes, shape_id):
    #Return shape by shape_id.#
    for shape in shapes:
        if shape.shape_id == shape_id:
            return shape
    return None

def find_shape_by_name(shapes, name):
    #Return shape by shape_id.#
    for shape in shapes:
        if shape.name == name:
            return shape
    return None
"""
        st.code(code_shapes, language="python")

        st.subheader('Human Number Format #2')

        human_code = """
# define human format func
def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
    """
        st.code(human_code, language='python')

    if option == "Tables":
        st.subheader('Format/Change PPT Table Font')

        table_font_code = """
def iter_cells(table):
    for row in table.rows:
        for cell in row.cells:
            yield cell

for cell in iter_cells(table_one):
    for paragraph in cell.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.size = Pt(8) """
        st.code(table_font_code, language='python')
