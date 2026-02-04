"""
Generate locked class templates for classes 3-9
Each template shows chapter names for all classes but locks content for non-registered classes
"""

templates = {
    3: {
        "title": "Class 3 — Computer Science",
        "description": "Theme: \"Computer se dosti — basics, etiquette, Paint & simple typing.\"",
        "chapters": [
            ("Computer Basics", "ict.svg", 1),
            ("Desktop & Peripherals", "https://images.unsplash.com/photo-1518779578993-ec3579fee39f?auto=format&fit=crop&w=800&q=60", 2),
            ("Paint Brush", "https://images.unsplash.com/photo-1526318472351-c75fcf0703ea?auto=format&fit=crop&w=800&q=60", 3),
            ("Keyboard & Typing Etiquette", "communication.svg", 4),
            ("Internet Safety", "https://images.unsplash.com/photo-1531497865142-7c9a6f0f5d71?auto=format&fit=crop&w=800&q=60", 5),
        ]
    },
    4: {
        "title": "Class 4 — Computer Science",
        "description": "Theme: \"Computer ki pehchan + Windows + Paint + Basic Office.\"",
        "chapters": [
            ("Computer Parts & Devices", "ict.svg", 1),
            ("Windows Basics", "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=60", 2),
            ("Paint (Creativity)", "https://images.unsplash.com/photo-1503602642458-232111445657?auto=format&fit=crop&w=800&q=60", 3),
            ("MS Word & PowerPoint Intro", "word-window.svg", 4),
        ]
    },
    5: {
        "title": "Class 5 — Computer Science",
        "description": "Theme: \"Office skills, Logo design, Internet ka safal use.\"",
        "chapters": [
            ("MS Office Essentials", "word-window.svg", 1),
            ("Logo Design & Drawing", "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=800&q=60", 2),
            ("Internet & Email Basics", "communication.svg", 3),
            ("Learning Resources Online", "https://images.unsplash.com/photo-1516321318423-f06f70a504f9?auto=format&fit=crop&w=800&q=60", 4),
        ]
    },
    6: {
        "title": "Class 6 — Computer Science",
        "description": "Theme: \"Digital skills, Office master + eCommerce intro.\"",
        "chapters": [
            ("Digital Literacy", "ict.svg", 1),
            ("Advanced Office Tools", "excel-window.svg", 2),
            ("Data & Spreadsheets", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=60", 3),
            ("eCommerce Basics", "https://images.unsplash.com/photo-1460925895917-adf4e565f900?auto=format&fit=crop&w=800&q=60", 4),
        ]
    },
    7: {
        "title": "Class 7 — Computer Science",
        "description": "Theme: \"HTML, Security awareness & Design basics.\"",
        "chapters": [
            ("HTML Fundamentals", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=60", 1),
            ("Web Page Design", "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=800&q=60", 2),
            ("Cybersecurity Basics", "https://images.unsplash.com/photo-1526374965328-7f5ae4e8e49e?auto=format&fit=crop&w=800&q=60", 3),
            ("Digital Ethics", "communication.svg", 4),
        ]
    },
    8: {
        "title": "Class 8 — Computer Science",
        "description": "Theme: \"Algorithms, Multimedia & eCommerce platforms.\"",
        "chapters": [
            ("Algorithm Design", "https://images.unsplash.com/photo-1516321318423-f06f70a504f9?auto=format&fit=crop&w=800&q=60", 1),
            ("Multimedia Creation", "https://images.unsplash.com/photo-1461749280684-ddefd3083d60?auto=format&fit=crop&w=800&q=60", 2),
            ("eCommerce Platforms", "https://images.unsplash.com/photo-1460925895917-adf4e565f900?auto=format&fit=crop&w=800&q=60", 3),
            ("Cloud Storage & Sharing", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=60", 4),
        ]
    },
    9: {
        "title": "Class 9 — Computer Science",
        "description": "Theme: \"Foundation for subject-specific digital skills.\"",
        "chapters": [
            ("Programming Basics", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=60", 1),
            ("Database Fundamentals", "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=60", 2),
            ("Web Development Intro", "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=800&q=60", 3),
            ("Information Security", "https://images.unsplash.com/photo-1526374965328-7f5ae4e8e49e?auto=format&fit=crop&w=800&q=60", 4),
        ]
    },
}

def generate_card_html(chapter_name, img_url, unit_num, class_num, is_static=False):
    """Generate HTML for a chapter card"""
    if is_static:
        img_src = "{% static 'images/" + img_url + "' %}"
    else:
        img_src = img_url
    
    html = '      <div class="col-6 col-md-3">\n'
    html += '        {% if is_locked %}\n'
    html += '        <div class="card h-100 opacity-75">\n'
    html += f'          <img src="{img_src}" class="card-img-top" alt="{chapter_name}">\n'
    html += '          <div class="card-body p-2">\n'
    html += f'            <p class="card-title mb-0 small">\n'
    html += f'              <i class="fa-solid fa-lock me-1" style="color: #dc3545;"></i>{chapter_name}\n'
    html += '            </p>\n'
    html += '          </div>\n'
    html += '          <button class="btn btn-sm btn-secondary w-100 disabled" disabled title="Content locked for your class">Locked</button>\n'
    html += '        </div>\n'
    html += '        {% else %}\n'
    html += f'        <a class="card h-100 text-decoration-none text-body" href="{{% url \'website:unit_detail\' {class_num} \'part-a\' {unit_num} %}}">\n'
    html += f'          <img src="{img_src}" class="card-img-top" alt="{chapter_name}">\n'
    html += '          <div class="card-body p-2">\n'
    html += f'            <p class="card-title mb-0 small">{chapter_name}</p>\n'
    html += '          </div>\n'
    html += '        </a>\n'
    html += '        {% endif %}\n'
    html += '      </div>\n'
    return html

def generate_template(class_num):
    """Generate complete template for a class"""
    config = templates[class_num]
    
    cards = ""
    for chapter_name, img_url, unit_num in config["chapters"]:
        is_static = not img_url.startswith("http")
        cards += generate_card_html(chapter_name, img_url, unit_num, class_num, is_static)
    
    template = "{% extends 'base.html' %}\n"
    template += "{% load static %}\n"
    template += "{% block content %}\n"
    template += "<section class=\"container py-4\">\n"
    template += "  <div class=\"row mb-3\">\n"
    template += "    <div class=\"col-md-8\">\n"
    template += f"      <h1>{config['title']}</h1>\n"
    template += f"      <p class=\"text-muted\">{config['description']}</p>\n"
    template += "      {% if is_locked %}\n"
    template += "      <div class=\"alert alert-warning mt-2 mb-0\" role=\"alert\">\n"
    template += "        <i class=\"fa-solid fa-lock me-2\"></i>This class content is <strong>locked</strong>. You can view chapter names but cannot access the content.\n"
    template += "      </div>\n"
    template += "      {% endif %}\n"
    template += "    </div>\n"
    template += "    <div class=\"col-md-4 text-md-end\">\n"
    template += "      <a class=\"btn btn-outline-secondary\" href=\"/\">← Back to Home</a>\n"
    template += f"      <a class=\"btn btn-outline-primary\" href=\"/classes/{class_num}/\">Refresh</a>\n"
    template += "    </div>\n"
    template += "  </div>\n"
    template += "  <div id=\"units\" class=\"mb-3\">\n"
    template += "    <h4>Chapters</h4>\n"
    template += "    <div class=\"row g-3\">\n"
    template += cards
    template += "    </div>\n"
    template += "  </div>\n"
    template += "</section>\n"
    template += "\n"
    template += "{% endblock %}\n"
    return template

# Generate and print templates
for class_num in range(3, 10):
    template_content = generate_template(class_num)
    print(f"=== CLASS {class_num} ===")
    print(template_content)
    print("\n\n")
