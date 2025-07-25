# FOAF RDF Data Generator

A Python tool for generating realistic FOAF (Friend of a Friend) RDF data in Turtle format, designed for demonstrations and testing. Perfect for creating sample datasets with professional networks and relationships.

## Features

- **Realistic Data**: Generates authentic-looking people with professional backgrounds
- **Industry Focus**: Includes real organizations from beverage, food, retail, advertising, and technology sectors
- **Professional Context**: Creates relevant job titles, skills, and interests for business demonstrations
- **Rich Relationships**: Builds social networks with bidirectional "knows" relationships
- **Multiple Formats**: Supports Turtle (TTL), XML, N3, and N-Triples output formats
- **Configurable**: Adjustable number of people and output options

## Installation

1. Clone or download this project
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Generate FOAF data with default settings (50 people):
```bash
python foaf_generator.py
```

### Advanced Usage

```bash
# Generate 100 people and save to custom file
python foaf_generator.py --count 100 --output my_foaf_data.ttl

# Generate in XML format
python foaf_generator.py --format xml --output foaf_data.xml

# Show help for all options
python foaf_generator.py --help
```

### Command Line Options

- `--output`, `-o`: Output filename (default: `foaf_data.ttl`)
- `--count`, `-c`: Number of people to generate (default: 50)
- `--format`, `-f`: Output format (`turtle`, `xml`, `n3`, `nt`)

## Sample Output

The generator creates Turtle files with rich FOAF data:

```turtle
@prefix ex: <http://example.org/people/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix org: <http://example.org/organizations/> .

ex:person_1 a foaf:Person ;
    foaf:firstName "Sarah" ;
    foaf:familyName "Johnson" ;
    foaf:name "Sarah Johnson" ;
    foaf:mbox <mailto:sarah.johnson@example.com> ;
    foaf:workplaceHomepage org:PepsiCo ;
    foaf:title "Brand Manager" ;
    foaf:knows ex:person_3, ex:person_15 ;
    foaf:interest [ rdfs:label "Marketing Strategy" ] ;
    foaf:topic_interest [ rdfs:label "Digital Marketing" ] .

org:PepsiCo a foaf:Organization ;
    foaf:name "PepsiCo" ;
    foaf:homepage <https://www.pepsico.com> ;
    rdfs:comment "Sector: Beverage" .
```

## Generated Data Structure

Each person includes:
- **Basic Info**: Name, email, optional phone number
- **Professional**: Workplace, job title, industry sector
- **Interests**: Marketing, sustainability, innovation topics
- **Skills**: Professional competencies relevant to business
- **Demographics**: Optional age information
- **Social**: Professional networking relationships
- **Web Presence**: Optional homepage/LinkedIn profiles

### Real Organizations Included

The generator includes authentic organizations across key sectors:

**Beverage Industry:**
- Coca-Cola, PepsiCo, Dr Pepper Snapple, Red Bull, Monster, Nestle Waters, Starbucks

**Consumer Goods & Food:**
- Unilever, P&G, Kraft Heinz, General Mills, Kellogg

**Retail & Distribution:**
- Walmart, Amazon, Target, Costco

**Marketing & Advertising:**
- WPP Group, Omnicom, Publicis, Interpublic

**Technology:**
- Microsoft, Google, Apple, Meta

## Use Cases

- **Business Demos**: Showcase semantic data platforms
- **Data Integration**: Test RDF data processing pipelines  
- **Knowledge Graphs**: Populate graph databases for development
- **Training**: Educational examples for RDF and FOAF concepts
- **Prototyping**: Quick datasets for proof-of-concept work

## Technical Details

- **Python 3.6+** required
- Uses `rdflib` for RDF generation and serialization
- Uses `faker` for realistic name and contact generation
- Follows FOAF vocabulary standards
- Generates valid Turtle syntax
- Creates bidirectional relationships for realistic networks

## File Structure

```
generate_foaf_data/
├── foaf_generator.py      # Main generator script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── sample_foaf_data.ttl  # Sample output
├── venv/                 # Virtual environment
└── semanticLayer/        # For git repository
    └── foafDataGen/
```

## License

MIT License - Feel free to use for commercial or educational purposes.

## Contributing

Contributions welcome! Areas for enhancement:
- Additional organization data
- More sophisticated relationship patterns
- Extended FOAF properties
- Alternative vocabularies (schema.org, etc.)
- Output format options 