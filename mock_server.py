
from fastapi import FastAPI

app = FastAPI()

@app.get("/linkedin/data")
async def get_linkedin_data(email: str):
  if email == "123":
    return None
  else: 
    return {
    "success": True,
    "credits_left": 4337,
    "rate_limit_left": 19608,
    "person": {
        "publicIdentifier": "julien-keraval-visum",
        "linkedInIdentifier": "ACoAACJrg3QBOHYEx_zMaj2sF7IgUFOpF5VLkss",
        "firstName": "Julien",
        "lastName": "Keraval",
        "headline": "COO @ Visum | Data Hunter",
        "location": "Paris, Île-de-France France",
        "photoUrl": "https://media.licdn.com/dms/image/C4D03AQEN7W54z8qsHQ/profile-displayphoto-shrink_800_800/0/1633355607781?e=1701907200&v=beta&t=79-W0gvK6hm_TK3liARic0iUnTYY1F6qbF_vkQV-ZoI",
        "creationDate": {
        "year": 2017
        },
        "followerCount": 6197,
        "connectionCount": 5747,
        "emails": [],
        "phoneNumbers": [],
        "positions": {
        "positionsCount": 6,
        "positionHistory": [
            {
            "startEndDate": {
                "start": {
                "month": 12,
                "year": 2020
                }
            },
            "title": "Co-founder & COO",
            "description": "Visum collects all the data you need to help your sales & marketing team",
            "companyName": "Visum ",
            "companyLocation": "Ville de Paris, Île-de-France, France",
            "companyLogo": "https://media.licdn.com/dms/image/C4E0BAQEbr48diDvnrw/company-logo_200_200/0/1674558570304?e=1704326400&v=beta&t=qk9thQBKgXOkog_Ii-EZF1NxdbSuCvUkQE4-u_TUNsY",
            "linkedInUrl": "https://www.linkedin.com/company/71234370/"
            },
            {
            "startEndDate": {
                "start": {
                "month": 3,
                "year": 2020
                }
            },
            "title": "Directeur marketing",
            "description": "Repos Digital recherche et sécurise les réseaux sociaux, boîtes mails et messageries après décès.",
            "companyName": "Repos Digital ",
            "companyLocation": "Paris Ouest La Défense",
            "companyLogo": "https://media.licdn.com/dms/image/C4D0BAQGBtwCMV-deCA/company-logo_200_200/0/1625094869961?e=1704326400&v=beta&t=YBIB_x52MvVB1gx4wQxr-r7I7O8yHPRuVz-fonyKpQs",
            "linkedInUrl": "https://www.linkedin.com/company/65841732/"
            },
            {
            "startEndDate": {
                "start": {
                "month": 9,
                "year": 2019
                },
                "end": {
                "month": 7,
                "year": 2020
                }
            },
            "title": "Engineering Project Manager",
            "companyName": "Safran",
            "companyLocation": "Vélizy-Villacoublay, Île-de-France, France",
            "companyLogo": "https://media.licdn.com/dms/image/C4D0BAQF12gJLvR-O3Q/company-logo_200_200/0/1519935017250?e=1704326400&v=beta&t=8L57xyEJPGaJ6CQhKq0i2mF5IsywCOZuUWGGNRPgeTk",
            "linkedInUrl": "https://www.linkedin.com/company/521777/"
            },
            {
            "startEndDate": {
                "start": {
                "month": 8,
                "year": 2017
                },
                "end": {
                "month": 9,
                "year": 2019
                }
            },
            "title": "Test Manager",
            "companyName": "Safran",
            "companyLocation": "Vélizy-Villacoublay, Île-de-France, France",
            "companyLogo": "https://media.licdn.com/dms/image/C4D0BAQF12gJLvR-O3Q/company-logo_200_200/0/1519935017250?e=1704326400&v=beta&t=8L57xyEJPGaJ6CQhKq0i2mF5IsywCOZuUWGGNRPgeTk",
            "linkedInUrl": "https://www.linkedin.com/company/521777/"
            },
            {
            "startEndDate": {
                "start": {
                "month": 9,
                "year": 2019
                },
                "end": {
                "month": 1,
                "year": 2020
                }
            },
            "contractType": "Self-employed",
            "title": "Développeur web / Webmarketing freelance",
            "description": "- Création de maquettes\n- Développement de site web\n- Intégration de module de paiement (workflow e-commerce et/ou Marketplace)\n- Intégration de module de livraison / expédition\n- Intégration de module de réservation\n- Mise en production de site web / application web\n- Configuration DNS\n- Creation d’application mobile native Android + IOS et mise en ligne sur les stores (avec gestion du workflow de test)\n- Configuration de serveur mail\n- Configuration de serveur web (Apache et/ou Ngnix)\n- Mise en place de funnel de conversion\n- Intégration CRM\n- Mise en place marketing automation\n- Amélioration du référencement Web (SEO)\n- Mise en place SEA (Search Engine Advertising)\n- Création et gestion de campagne de PUB sur les réseaux sociaux\n- Création et gestion de blog entreprise (content marketing) => Ecriture, diffusion, analyse\n- Monitoring et maintenance de serveur web\n- Evolution de site / application web existant\n- Migration d’hébergeur web\n- Conseil Marketing, Business, Informatique etc.\n- Formation à différent langage de développement web (html5, css, JavaScript, PHP …)\n- Formation à différent Framework de développement web (Laravel, Vue.js, node.js, express.js, bootstrap, Vuetify…)\n- Formation à différent CMS (WordPress, WooCommerce …)",
            "companyName": "Malt ",
            "companyLocation": "Ville de Paris, Île-de-France, France",
            "companyLogo": "https://media.licdn.com/dms/image/D4E0BAQE6sdo2FBxl2Q/company-logo_200_200/0/1689250164264?e=1704326400&v=beta&t=bwUHhylNGcXOipjwBMyFGzJKnx5Vl_l3-DUddjLcu8c",
            "linkedInUrl": "https://www.linkedin.com/company/5285846/"
            },
            {
            "startEndDate": {
                "start": {
                "month": 9,
                "year": 2015
                },
                "end": {
                "month": 8,
                "year": 2017
                }
            },
            "title": "Assistant chef d'exploitation",
            "companyName": "GRDF",
            "companyLocation": "Villeneuve-le-Roi, Île-de-France, France",
            "companyLogo": "https://media.licdn.com/dms/image/C4E0BAQFbrgye86-8pw/company-logo_200_200/0/1671574027730?e=1704326400&v=beta&t=GPrlvhxJCtiPI2PgOBLs-OOXEtbiRmWZdA5BClbHAdI",
            "linkedInUrl": "https://www.linkedin.com/company/1037919/"
            }
        ]
        },
        "schools": {
        "educationsCount": 2,
        "educationHistory": [
            {
            "startEndDate": {
                "start": {
                "year": 2017
                },
                "end": {
                "year": 2020
                }
            },
            "schoolName": "ESILV - Ecole Supérieure d'Ingénieurs Léonard de Vinci",
            "description": "The IBO Major trains general IT engineers, able to master all components of information processing. To meet the changing strategic needs of the company, the future engineer will be trained in information systems, database architecture, mobility and application development.\n\nProgram Overview\nComputers, Big Data and Connected Objects\n\n• ADVANCED SOFTWARE DEVELOPMENT: Architecture & Programming, Advanced Data Structures and Algorithms, Software Development Process, Java EE & Frameworks; Mobile Application development, Web Application Architectures;\n• DATABASES: Advanced Topics in NoSQL Databases, Advanced Database Management;\n• BIG DATA: Machine Learning and Clustering;\n• NETWORKS: Network Management & Security;\n• INFORMATION SYSTEMS: Cloud computing & Datacenters, IT management, B.I. SAP;\n• INFORMATION PROCESSING: Parallel computing, Multimedia Information Processing;\n• EMBEDDED SYSTEMS: Embedded Systems.",
            "degreeName": "Diplôme d'ingénieur, Informatique, Big data et Objets connectés",
            "fieldOfStudy": "Diplôme d'ingénieur, Informatique, Big data et Objets connectés",
            "schoolLogo": "https://media.licdn.com/dms/image/C560BAQF-voGLcZoK6w/company-logo_200_200/0/1642158124302?e=1704326400&v=beta&t=mSoLd4M_OiQ2zuzoycEcFaKV9-bjxMMpnw-PeIMRb6k",
            "linkedInUrl": "https://www.linkedin.com/company/15142508/"
            },
            {
            "schoolName": "Pepite x Schoolab",
            "description": "Pépite Start’up Ile-de-France a été créé par les PÉPITE franciliens et par Pépite Île-de-France, avec le le soutien de la Région Ile-de-France, en collaboration avec le Schoolab. Il est conçu pour les Étudiants-Entrepreneurs des PÉPITE franciliens.\n\nC’est un programme d’accompagnement early stage pendant lesquels vous travaillez à 100 % à sur votre projet de création.\n\nPÉPITE Start’up vous emmène sur le terrain pour confronter votre idée au marché, prototyper et tester votre produit pour qu’il devienne un business. Vous rencontrez des experts pour vous challenger et participez à des ateliers pour monter en compétences, le tout dans un espace de travail unique à Station F.",
            "degreeName": "Pepite Start'up IDF at Station F, Entrepreneuriat / études entrepreneuriales",
            "fieldOfStudy": "Pepite Start'up IDF at Station F, Entrepreneuriat / études entrepreneuriales",
            "schoolLogo": None,
            "linkedInUrl": None
            }
        ]
        },
        "skills": [
        "Reverse Contact",
        "Développement d’API",
        "Marketing numérique",
        "Lean Startup",
        "Gestion du changement",
        "Testing",
        "Optimisation des moteurs de recherche (SEO)",
        "Marketing par moteur de recherche (SEM)",
        "Marketing sur les médias sociaux",
        "Programmation",
        "Tests de systèmes",
        "HP Quality Center",
        "JavaScript",
        "HTML5",
        "CSS",
        "SAP",
        "MongoDB",
        "NoSQL",
        "Python",
        "SQL"
        ],
        "languages": [
        "Anglais",
        "Français"
        ]
    },
    "company": {
        "websiteUrl": "https://visum.run",
        "name": "Visum",
        "logo": "https://media.licdn.com/dms/image/C4E0BAQEbr48diDvnrw/company-logo_200_200/0/1674558570304?e=1704326400&v=beta&t=qk9thQBKgXOkog_Ii-EZF1NxdbSuCvUkQE4-u_TUNsY",
        "employeeCount": 8,
        "description": "In other words “the mister gadget” of Data enrichment.\n\nWe specialize in hunting down all types of data for your business - with over 5 years of experience and already 3 enrichment tools created, we're dedicated to providing you with the most comprehensive and up-to-date data possible, no matter how complex or difficult it may be to get it.\n\nTrust us to be your data hunting experts and help you stay ahead of the competition.",
        "tagline": "Data Hunter for companies",
        "specialities": [
        "Lead Generation",
        "Lead Qualification",
        "Market Search",
        "Competitor analysis",
        "CRM enrichment"
        ],
        "headquarter": {
        "country": "FR",
        "geographicArea": "Île-de-France",
        "city": "Paris",
        "postalCode": "75013"
        },
        "industry": "Technology, Information and Internet",
        "universalName": "visum-run",
        "linkedinUrl": "https://www.linkedin.com/company/visum-run/",
        "linkedinId": "71234370"
    }
    }