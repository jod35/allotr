from lxml import etree


with open('index.html', 'r') as f:
    html_content = f.read()

# Parse the HTML using lxml
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Find and extract course-related data from the anchor tags
# Here, you need to identify the specific XPath or CSS selector that represents the course information
# inside the anchor tags. For example, if course information is contained within <a> tags with class "course-link",
# you can use:
course_anchors = tree.xpath('//a[contains(@class, "aalink")]')

# Process each anchor tag to extract the course data
for anchor in course_anchors:
    course_title = anchor.xpath('text()')[0]  # Extract the text inside the anchor tag as the course title
    course_url = anchor.xpath('@href')[0]      # Extract the URL (href attribute) of the anchor tag as the course URL


    print(course_title)
    print(course_url)
        # Here, you can process the extracted data as per your requirements.
        # For example, you can store it in a data structure or save it to a file.

    # If you want to save the extracted data to a file, you can do it here.
    # For example:
    # with open('extracted_courses.txt', 'w') as f:
    #     for anchor in course_anchors:
    #         course_title = anchor.xpath('text()')[0]
    #         course_url = anchor.xpath('@href')[0]
    #         f.write(f"Course Title: {course_title}, URL: {course_url}\n")


