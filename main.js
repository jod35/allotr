function convertToNestedStructure(flatData) {
    const nestedData = [];
  
    for (const item of flatData) {
      const { lecturer, courses } = item;
  
      const lecturerObj = {
        name: lecturer,
        _children: courses.map(course => ({ name: course }))
      };
  
      nestedData.push(lecturerObj);
    }
  
    console.log(nestedData);
}

const data = [
    {
        "lecturer": "Timothy Kivumbi",
        "courses": [
            "Computer Applications & Systems",
            "Internet Technology & Website Design",
            "Operating Systems",
            "Computer Forensic Tools",
            "Operating Systems Forensics",
            "Evidence Handling and Presentation",
            "Survey of Operating Systems"
        ]
    },
    {
        "lecturer": "Simon Peter Kabiito",
        "courses": []
    },
    {
        "lecturer": "Mary Komunte",
        "courses": [
            "Management Information Systems",
            "Systems Analysis & Design"
        ]
    },
    {
        "lecturer": "Allan Ninyesiga",
        "courses": [
            "Principles of Programming",
            "Research Methods",
            "Artiﬁcial Intelligence",
            "Practicum: Data Science"
        ]
    },
    {
        "lecturer": "Fred Paul Mark Jjunju",
        "courses": [
            "Data Structures & Algorithms"
        ]
    },
    {
        "lecturer": "Rehema Atugonza",
        "courses": [
            "Data Warehousing",
            "Computer Forensics",
            "Automata & Computability"
        ]
    },
    {
        "lecturer": "Asad Seguya",
        "courses": [
            "Computer Systems Security",
            "Software Engineering Principles",
            "Computer Architecture",
            "Software construction"
        ]
    },
    {
        "lecturer": "William Ahamya",
        "courses": [
            "Multimedia Applications"
        ]
    },
    {
        "lecturer": "Muzzah Zedekiya",
        "courses": [
            "Systems Administration",
            "Network Security",
            "Networking & Cabling",
            "CS 106 Hardware Maintenance & Repair"
        ]
    },
    {
        "lecturer": "Hillary Kaluuma",
        "courses": [
            "Mobile Applications Programming",
            "Event Driven programming"
        ]
    },
    {
        "lecturer": "Andrew Beriisa",
        "courses": [
            "Project Planning & Management",
            "Software Project Management",
            "Criminal Profiling"
        ]
    },
    {
        "lecturer": "Isaac Mukonyezi",
        "courses": [
            "Probability & Statistics",
            "Computer Networks & Data Communications"
        ]
    },
    {
        "lecturer": "Gloria Mutuwa",
        "courses": [
            "Business Law",
            "Psychology of Abnormal Behavior"
        ]
    }
]

convertToNestedStructure(data)