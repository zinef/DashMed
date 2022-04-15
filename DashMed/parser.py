
article = {
  "MedlineCitation": {
    "GeneralNote": [],
    "OtherAbstract": [],
    "OtherID": [],
    "CitationSubset": [
      "IM"
    ],
    "KeywordList": [
      [
        "Anxiety",
        "Child",
        "Fever",
        "Parents",
        "Simulation education"
      ]
    ],
    "SpaceFlightMission": [],
    "PMID": "33823379",
    "DateCompleted": {
      "Year": "2021",
      "Month": "12",
      "Day": "08"
    },
    "DateRevised": {
      "Year": "2021",
      "Month": "12",
      "Day": "14"
    },
    "Article": {
      "ELocationID": [
        "S0882-5963(21)00094-4",
        "10.1016/j.pedn.2021.03.024"
      ],
      "Language": [
        "eng"
      ],
      "ArticleDate": [
        {
          "Year": "2021",
          "Month": "04",
          "Day": "03"
        }
      ],
      "Journal": {
        "ISSN": "1532-8449",
        "JournalIssue": {
          "Volume": "61",
          "PubDate": {
            "MedlineDate": "2021 Nov-Dec"
          }
        },
        "Title": "Journal of pediatric nursing",
        "ISOAbbreviation": "J Pediatr Nurs"
      },
      "ArticleTitle": "Efficacy of Scenario Simulation-Based Education in Relieving Parental Anxiety about Fever in Children.",
      "Pagination": {
        "MedlinePgn": "102-108"
      },
      "Abstract": {
        "AbstractText": [
          "This study was designed to evaluate the short- and long-term effects of a scenario simulation-based education intervention on parental anxiety about fever in their children.",
          "This experimental research was conducted using a two-group pretest-posttest design. One hundred and sixty parents of 3-month to 5-year-old children enrolled in preschools and kindergartens with childcare services were recruited as participants using cluster random sampling. The participants were divided randomly into an experimental group (80) and a control group (80). The former participated in a scenario simulation-based education intervention and received a fever education booklet. The latter received the booklet only. Data were collected using the Children's Fever Anxiety Inventory at three time points: before the intervention (pretest, T1) and at six-month (T2) and 12-month (T3) posttests.",
          "Significant intergroup differences in fever anxiety were found at both T2 and T3 (p < .001). For both groups, the scores at T2 and T3 were significantly lower than at T1 (p < .001) and the difference between T2 and T3 did not attain statistical significance (p > .05). Although both groups experienced reduced fever anxiety over time, this reduction was significantly greater in the experimental group than in the control group (p < .001).",
          "Simulation-based education may be used in conjunction with the traditional fever education booklet to further reduce parent fever anxiety over time.",    
          "This simulation-based education approach significantly and positively impacts parental anxiety about fever in their children. Furthermore, the approach may be generalizable to other childhood healthcare settings."
        ],
        "CopyrightInformation": "Copyright \u00a9 2021 Elsevier Inc. All rights reserved."
      },
      "AuthorList": [
        {
          "AffiliationInfo": [
            {
              "Identifier": [],
              "Affiliation": "Department of Nursing, National Tainan Junior College of Nursing, Taiwan. Electronic address: fabchuan@ntin.edu.tw."
            }
          ],
          "Identifier": [],
          "LastName": "Chang",
          "ForeName": "Li Chuan",
          "Initials": "LC"
        },
        {
          "AffiliationInfo": [
            {
              "Identifier": [],
              "Affiliation": "Department of Nursing, National Tainan Junior College of Nursing, Taiwan; Department of Nursing, College of Medicine, National Cheng Kung University, Taiwan. Electronic address: meay@mail.ncku.edu.tw."
            }
          ],
          "Identifier": [],
          "LastName": "Huang",
          "ForeName": "Mei Chih",
          "Initials": "MC"
        }
      ],
      "PublicationTypeList": [
        "Journal Article",
        "Randomized Controlled Trial"
      ]
    },
    "MedlineJournalInfo": {
      "Country": "United States",
      "MedlineTA": "J Pediatr Nurs",
      "NlmUniqueID": "8607529",
      "ISSNLinking": "0882-5963"
    },
    "MeshHeadingList": [
      {
        "QualifierName": [
          "prevention & control"
        ],
        "DescriptorName": "Anxiety"
      },
      {
        "QualifierName": [],
        "DescriptorName": "Anxiety Disorders"
      },
      {
        "QualifierName": [],
        "DescriptorName": "Child"
      },
      {
        "QualifierName": [],
        "DescriptorName": "Child, Preschool"
      },
      {
        "QualifierName": [
          "therapy"
        ],
        "DescriptorName": "Fever"
      },
      {
        "QualifierName": [],
        "DescriptorName": "Humans"
      },
      {
        "QualifierName": [],
        "DescriptorName": "Pamphlets"
      },
      {
        "QualifierName": [],
        "DescriptorName": "Parents"
      }
    ],
    "CoiStatement": "Declaration of Competing Interest None."
  },
  "PubmedData": {
    "ReferenceList": [],
    "History": [
      {
        "Year": "2020",
        "Month": "09",
        "Day": "24"
      },
      {
        "Year": "2021",
        "Month": "03",
        "Day": "25"
      },
      {
        "Year": "2021",
        "Month": "03",
        "Day": "25"
      },
      {
        "Year": "2021",
        "Month": "4",
        "Day": "7",
        "Hour": "6",
        "Minute": "0"
      },
      {
        "Year": "2021",
        "Month": "12",
        "Day": "15",
        "Hour": "6",
        "Minute": "0"
      },
      {
        "Year": "2021",
        "Month": "4",
        "Day": "6",
        "Hour": "20",
        "Minute": "15"
      }
    ],
    "PublicationStatus": "ppublish",
    "ArticleIdList": [
      "33823379",
      "S0882-5963(21)00094-4",
      "10.1016/j.pedn.2021.03.024"
    ]
  }
}

class Parser:

    def __init__(self) -> None:
        pass

    def extract_parsed_article_text(self,article):
        d = self.parse_article(article)
        ArticleTitle = d['ArticleTitle']
        AbstractText = ' '.join(d['AbstractText'])

        text = ArticleTitle + " " + AbstractText
        return text


    def parse_article(self,article):
        #get the title and the abstract text 
        parsing_fun_title=self.get_right_function('ArticleTitle')
        parsing_fun_abstract=self.get_right_function('AbstractText')
        d = {
            'ArticleTitle':parsing_fun_title(article),
            'AbstractText':parsing_fun_abstract(article)
        }
        return d

    def get_right_function(self,name):
        return{
            'MedlineCitation' : self.parse_MedLineCitation,
            'KeywordList': self.parse_KeywordList,
            'DateCompleted': self.parse_DateCompleted,
            'DateRevised': self.parse_DateRevised,
            'Article': self.parse_Article,
            'ELocationID': self.parse_ELocationID,
            'Language' : self.parse_Language,
            'ArticleDate' : self.parse_ArticleDate,
            'ArticleTitle' : self.parse_ArticleTitle,
            'AbstractText' : self.parse_AbstractText,
            #it's flexible & we can add as many as we want or need 
        }.get(name) or None

    def parse_MedLineCitation(self,article):
        return article['MedlineCitation']

    def parse_KeywordList(self,article):
        return article['MedlineCitation']['KeywordList']

    def parse_DateCompleted(self,article):
        return article['MedlineCitation']['DateCompleted']
    
    def parse_DateRevised(self,article):
        return article['MedlineCitation']['DateRevised']

    def parse_Article(self,article):
        return article['MedlineCitation']['Article']

    def parse_ELocationID(self,article):
        return article['MedlineCitation']['Article']['ELocationID']

    def parse_Language(self,article):
        return article['MedlineCitation']['Article']['Language']

    def parse_ArticleDate(self,article):
        return article['MedlineCitation']['Article']['ArticleDate']

    def parse_ArticleTitle(self,article):
        return article['MedlineCitation']['Article']['ArticleTitle']

    def parse_AbstractText(self,article):
        return article['MedlineCitation']['Article']['Abstract']['AbstractText']

    
parser = Parser()

# print(parser.extract_parsed_article_text(article))