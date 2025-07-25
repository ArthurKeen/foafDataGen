#!/usr/bin/env python3
"""
FOAF (Friend of a Friend) RDF Data Generator
Generates realistic FOAF data in Turtle format for demonstrations

Usage:
    python foaf_generator.py [--output OUTPUT_FILE] [--count COUNT]
"""

import argparse
import random
from datetime import datetime, timedelta
from faker import Faker
from rdflib import Graph, Namespace, Literal, URIRef, BNode
from rdflib.namespace import RDF, RDFS, XSD, FOAF


class FOAFDataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.graph = Graph()
        
        # Define namespaces
        self.foaf = FOAF
        self.ex = Namespace("http://example.org/people/")
        self.org = Namespace("http://example.org/organizations/")
        
        # Bind prefixes for readable output
        self.graph.bind("foaf", self.foaf)
        self.graph.bind("ex", self.ex)
        self.graph.bind("org", self.org)
        self.graph.bind("xsd", XSD)
        
        # Real organizations with focus on beverage industry and related sectors
        self.organizations = [
            # Beverage Companies
            {"name": "PepsiCo", "sector": "Beverage", "website": "https://www.pepsico.com"},
            {"name": "The Coca-Cola Company", "sector": "Beverage", "website": "https://www.coca-colacompany.com"},
            {"name": "Dr Pepper Snapple Group", "sector": "Beverage", "website": "https://www.drpeppersnapplegroup.com"},
            {"name": "Red Bull GmbH", "sector": "Beverage", "website": "https://www.redbull.com"},
            {"name": "Monster Beverage Corporation", "sector": "Beverage", "website": "https://www.monsterbevcorp.com"},
            {"name": "Nestle Waters", "sector": "Beverage", "website": "https://www.nestle.com"},
            {"name": "Starbucks Corporation", "sector": "Beverage", "website": "https://www.starbucks.com"},
            
            # Food & CPG Companies
            {"name": "Unilever", "sector": "Consumer Goods", "website": "https://www.unilever.com"},
            {"name": "Procter & Gamble", "sector": "Consumer Goods", "website": "https://www.pg.com"},
            {"name": "Kraft Heinz", "sector": "Food", "website": "https://www.kraftheinzcompany.com"},
            {"name": "General Mills", "sector": "Food", "website": "https://www.generalmills.com"},
            {"name": "Kellogg Company", "sector": "Food", "website": "https://www.kelloggcompany.com"},
            
            # Retail & Distribution
            {"name": "Walmart Inc.", "sector": "Retail", "website": "https://www.walmart.com"},
            {"name": "Amazon", "sector": "Technology/Retail", "website": "https://www.amazon.com"},
            {"name": "Target Corporation", "sector": "Retail", "website": "https://www.target.com"},
            {"name": "Costco Wholesale", "sector": "Retail", "website": "https://www.costco.com"},
            
            # Marketing & Advertising
            {"name": "WPP Group", "sector": "Advertising", "website": "https://www.wpp.com"},
            {"name": "Omnicom Group", "sector": "Advertising", "website": "https://www.omnicomgroup.com"},
            {"name": "Publicis Groupe", "sector": "Advertising", "website": "https://www.publicisgroupe.com"},
            {"name": "Interpublic Group", "sector": "Advertising", "website": "https://www.interpublic.com"},
            
            # Technology Companies
            {"name": "Microsoft Corporation", "sector": "Technology", "website": "https://www.microsoft.com"},
            {"name": "Google LLC", "sector": "Technology", "website": "https://www.google.com"},
            {"name": "Apple Inc.", "sector": "Technology", "website": "https://www.apple.com"},
            {"name": "Meta Platforms", "sector": "Technology", "website": "https://www.meta.com"}
        ]
        
        # Job titles relevant to beverage industry and marketing
        self.job_titles = [
            "Chief Marketing Officer", "Brand Manager", "Product Manager", "Digital Marketing Director",
            "Supply Chain Manager", "Sales Director", "Category Manager", "Trade Marketing Manager",
            "Consumer Insights Manager", "Innovation Director", "Sustainability Manager",
            "Channel Development Manager", "Regional Sales Manager", "Marketing Analytics Manager",
            "Brand Strategy Director", "Customer Marketing Manager", "Portfolio Manager",
            "Business Development Manager", "Market Research Analyst", "Communications Director"
        ]
        
        self.interests = [
            "Marketing Strategy", "Brand Development", "Consumer Psychology", "Digital Transformation",
            "Sustainability", "Supply Chain Optimization", "Data Analytics", "Innovation Management",
            "Customer Experience", "Market Research", "Social Media Marketing", "Content Strategy",
            "E-commerce", "Retail Strategy", "Product Development", "Consumer Trends",
            "Competitive Intelligence", "Partnership Development", "Crisis Management"
        ]
        
        self.skills = [
            "Strategic Planning", "Brand Management", "Digital Marketing", "Data Analysis",
            "Project Management", "Leadership", "Market Research", "Consumer Insights",
            "Partnership Development", "Innovation", "Cross-functional Collaboration",
            "Budget Management", "Trend Analysis", "Customer Segmentation", "Campaign Management"
        ]
    
    def create_organization(self, org_data):
        """Create an organization in the RDF graph"""
        org_uri = self.org[org_data["name"].replace(" ", "_").replace(".", "").replace("&", "and")]
        
        self.graph.add((org_uri, RDF.type, self.foaf.Organization))
        self.graph.add((org_uri, self.foaf.name, Literal(org_data["name"])))
        
        if org_data.get("website"):
            self.graph.add((org_uri, self.foaf.homepage, URIRef(org_data["website"])))
        
        if org_data.get("sector"):
            # Use RDFS comment for sector information
            self.graph.add((org_uri, RDFS.comment, Literal(f"Sector: {org_data['sector']}")))
        
        return org_uri
    
    def create_person(self, person_id):
        """Create a person with realistic professional information"""
        person_uri = self.ex[f"person_{person_id}"]
        
        # Basic person information
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        full_name = f"{first_name} {last_name}"
        email = f"{first_name.lower()}.{last_name.lower()}@{self.fake.domain_name()}"
        
        # Add basic FOAF properties
        self.graph.add((person_uri, RDF.type, self.foaf.Person))
        self.graph.add((person_uri, self.foaf.firstName, Literal(first_name)))
        self.graph.add((person_uri, self.foaf.familyName, Literal(last_name)))
        self.graph.add((person_uri, self.foaf.name, Literal(full_name)))
        self.graph.add((person_uri, self.foaf.mbox, URIRef(f"mailto:{email}")))
        
        # Add phone (sometimes)
        if random.random() < 0.7:
            self.graph.add((person_uri, self.foaf.phone, URIRef(f"tel:{self.fake.phone_number()}")))
        
        # Add workplace
        org_data = random.choice(self.organizations)
        org_uri = self.create_organization(org_data)
        self.graph.add((person_uri, self.foaf.workplaceHomepage, org_uri))
        
        # Add job title
        job_title = random.choice(self.job_titles)
        self.graph.add((person_uri, self.foaf.title, Literal(job_title)))
        
        # Add interests
        num_interests = random.randint(2, 5)
        selected_interests = random.sample(self.interests, num_interests)
        for interest in selected_interests:
            interest_node = BNode()
            self.graph.add((person_uri, self.foaf.interest, interest_node))
            self.graph.add((interest_node, RDFS.label, Literal(interest)))
        
        # Add skills using topic_interest
        num_skills = random.randint(3, 7)
        selected_skills = random.sample(self.skills, num_skills)
        for skill in selected_skills:
            skill_node = BNode()
            self.graph.add((person_uri, self.foaf.topic_interest, skill_node))
            self.graph.add((skill_node, RDFS.label, Literal(skill)))
        
        # Add age (sometimes)
        if random.random() < 0.6:
            age = random.randint(25, 65)
            self.graph.add((person_uri, self.foaf.age, Literal(age, datatype=XSD.integer)))
        
        # Add homepage (sometimes)
        if random.random() < 0.4:
            homepage = f"https://www.linkedin.com/in/{first_name.lower()}-{last_name.lower()}"
            self.graph.add((person_uri, self.foaf.homepage, URIRef(homepage)))
        
        return person_uri
    
    def add_relationships(self, people):
        """Add knows relationships between people"""
        for person in people:
            # Each person knows 2-8 other people
            num_friends = random.randint(2, min(8, len(people) - 1))
            friends = random.sample([p for p in people if p != person], num_friends)
            
            for friend in friends:
                self.graph.add((person, self.foaf.knows, friend))
                # Make some relationships bidirectional
                if random.random() < 0.7:
                    self.graph.add((friend, self.foaf.knows, person))
    
    def generate_data(self, num_people=50):
        """Generate FOAF data for specified number of people"""
        print(f"Generating FOAF data for {num_people} people...")
        
        # Create people
        people = []
        for i in range(num_people):
            person_uri = self.create_person(i + 1)
            people.append(person_uri)
        
        # Add relationships
        self.add_relationships(people)
        
        print(f"Generated {len(people)} people with relationships")
        print(f"Total triples: {len(self.graph)}")
        
        return self.graph
    
    def save_to_file(self, filename, format_type="turtle"):
        """Save the graph to a file"""
        self.graph.serialize(destination=filename, format=format_type)
        print(f"Data saved to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Generate FOAF RDF data")
    parser.add_argument("--output", "-o", default="foaf_data.ttl", 
                       help="Output filename (default: foaf_data.ttl)")
    parser.add_argument("--count", "-c", type=int, default=50,
                       help="Number of people to generate (default: 50)")
    parser.add_argument("--format", "-f", default="turtle",
                       choices=["turtle", "xml", "n3", "nt"],
                       help="Output format (default: turtle)")
    
    args = parser.parse_args()
    
    # Generate data
    generator = FOAFDataGenerator()
    generator.generate_data(args.count)
    
    # Save to file
    generator.save_to_file(args.output, args.format)
    
    print(f"\nFOAF data generation complete!")
    print(f"File: {args.output}")
    print(f"Format: {args.format}")
    print(f"People: {args.count}")


if __name__ == "__main__":
    main() 