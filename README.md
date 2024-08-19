
# Decision_Making

## Description
decision_making is a Python 3 library for solving Fuzzy-Multi Criteria Decision Making (Fuzzy-MCDM) problems.

The implementation of fuzzy logic in MCDM techniques has enhanced capabilities, allowing users to provide assessments not only in discrete values but also in linguistic forms that include ranges. Through this, we can assess multiple result without having the need to have complete conformity.

Link for documnents and research paper: [docxdecison-making](https://github.com/iamAnas-zzx/decision_making/tree/main/docx_words)

---

## Table of Contents 

- [Installation](#installation)
- [Important Links](#important-links)
- [Available Methods](#available-methods)
- [Usage](#usage)
- [Features](#features)
- [Credits](#credits)
- [Refernences](#references)
- [License](#license)

---

## Installation

### Requirements

decision_making requires:

- Python (>= 3.12.1)
- NumPy (>= 1.26.4)
- SciPy (>= 1.13.0)
- Pandas (>= 2.2.2)

### User installation

You can simply download and install decision_making by: 
```bash
pip install decision_making
```

---

## Important Links

- Official source code repo: https://github.com/iamAnas-zzx/decision_making.git
- Official research paper: https://github.com/iamAnas-zzx/decision_making/tree/main/research_paper

---

## Available Methods

The library conatins methods with there docx links:

|  Acronym            	|  Method Name                                                                      |                Links                |
| :-------------------- | --------------------------------------------------------------------------------- | :--------------------------------------: |
|  AHP             	|  Analytic Hierarchy Process         |               [Link](https://github.com/iamAnas-zzx/decision_making/blob/main/docx_words/AHP.docx)                 |
|  TOPSIS              	|  Technique for the Order of Prioritisation by Similarity to Ideal Solution                |               [Link](https://github.com/iamAnas-zzx/decision_making/blob/main/docx_words/TOPSIS.docx)                 |
|  COPRAS             	|  Complex Proportional Assessment                                                  |               [Link](https://github.com/iamAnas-zzx/decision_making/blob/main/docx_words/COPRAS.docx)                 |
|  Fuzzy-AHP        	|  Fuzzy - Analytic Hierarchy Process      |   [Link](https://github.com/iamAnas-zzx/decision_making/blob/main/docx_words/Fuzzy-AHP.docx)      |
|  Fuzzy-TOPSIS              	|  Fuzzy - Technique for the Order of Prioritisation by Similarity to Ideal Solution    |               [Link](https://github.com/iamAnas-zzx/decision_making/blob/main/docx_words/Fuzzy-TOPSIS.docx)                 |
|  Fuzzy-COPRAS             	|  Fuzzy - Complex Proportional Assessment                                |               [Link](https://github.com/iamAnas-zzx/decision_making/blob/main/docx_words/Fuzzy-COPRAS%20.docx)                 |


## Usage

Here's a example of how use this library to solve AHP problem.
For more examples on how to use different methods with explanation see the docx of [methods](https://github.com/iamAnas-zzx/decision_making/tree/main/docx_words).

```python

    #importing necessary requirements
    import numpy as np
    from decision_making import ahp
    '''
    Here I provide the criteria names and alternative names
    The order is strict so please provide list of strings
    '''
    criteria_names=["Experience", "Education", "Charisma", "Age"]
    alternative_names=["Tom", "Rick", "Harry"]

    '''
    The data provided is in the form of comparision between two terms.
    In the example we have 4 matrix where the comparision between alternatives is made using a specific criteria.
    They are stacked in a 3d tensor so that more parallelism operations can be achieved.
    And we have a criteria comparision matrix where the comparision between criterias is made.(This can also contain weights in 1d numpy array)
    '''
    criteria1 = np.array([[1,1/4,4],
    [4,1,9],[1/4,1/9,1]])
    criteria2 = np.array([[1,3,1/5],
    [1/3,1,1/7],[5,7,1]])
    criteria3 = np.array([[1,5,9],
    [1/5,1,4],[1/9,1/4,1]])
    criteria4 = np.array([[1,1/3,5],
    [3,1,9],[1/5,1/9,1]])

    # list of matrix containing alternative to alternative comparision 
    # for every single criteria
    matrix_per_criteria=np.array([criteria1, criteria2, criteria3, criteria4]) 
    
    # criteria comparison matrix
    criteria_comparison=np.array([[1,4,3,7], [1/4,1,1/3,3], [1/3,3,1,5],[1/7,1/3,1/5,1]])
    
    # Evaluting and getting answer
    ahp(criteria_names,alternative_names,matrix_per_criteria,criteria_comparison,
    print_weight_matrix=True)

    # Alternatively creating an object
    a = ahp(criteria_names, alternative_names, matrix_per_criteria, criteria_comparison,
    print_weight_matrix=True)

```

---

## Features

Here's an example of additional features of this library are:
For more examples on how to use additional features with explanation see the docx of [methods](https://github.com/iamAnas-zzx/decision_making/tree/main/docx_words).


```python

    # After creating an object for a particular methods 
    # we can check different attributes to analyze the procedure of the method
    a = ahp(criteria_names, alternative_names, matrix_per_criteria, criteria_comparison,
    print_weight_matrix=True)

    # different attributes are-
    a.normalized_unweighted_matrix

    a.weighted_matrix

    a.most_suitable_alternative

    a.rank_array


```

---

## Credits

List of our collaborators:

- Ahmad Anas - [github](https://github.com/iamAnas-zzx/)
- Eeshan Anand - [github](https://github.com/EESHAN-ANAND-2002)
---

## References

<a name="ref1">**[1]**</a> P. Audebert, P. Hapiot, J. Electroanal. Chem. 361 (1993) 177. 

<a name="ref1">**[2]**</a> Giorgio Nordo, Saeid Jafari, Arif Mehmood and Bhimraj Basumatary (2024),   A Python Framework f¬or Neutrosophic Sets and Mappings.

<a name="ref1">**[3]**</a> Haitham A. El-Ghareeb (2019), Novel Open Source Python Neutrosophic Package.

<a name="ref1">**[4]**</a> Bartłomiej Kizielewicz, Andrii Shekhovtsov , Wojciech Sałabun (2023),  pymcdm—The universal library for solving multi-criteria decision-making problems.

<a name="ref1">**[5]**</a> Rakesh Ranjan Kumar, Siba Mishra, Chiranjeev Kumar(2017), Prioritizing the solution of cloud service selection using integrated MCDM methods under Fuzzy environment.

<a name="ref1">**[6]**</a> Sudha.S, Edwin Deepak F.X, Nivetha Martin(2023), Integrated Machine Learning Algorithms and MCDM Techniques in Optimal Ranking of Battery Electric Vehicles

<a name="ref1">**[7]**</a> Alaa Alden Al Mohamed, Sobhi Al Mohamed and Moustafa Zino (2023),  Application of fuzzy multicriteria decision-making model in selecting pandemic hospital site.

<a name="ref1">**[8]**</a> İhsan Kayaa,  Murat Çolakb , Fulya Terzi (2019), A comprehensive review of fuzzy multi criteria decision making methodologies for energy policy making.

<a name="ref1">**[9]**</a> Zhang, Y.J.; Sun, Y.F.; Huang, J(2018), Energy efficiency, carbon emission performance, and technology gaps: Evidence from CDM project investment. 

<a name="ref1">**[10]**</a> Javed, M.S.; Ma, T.; Jurasz, J.; Canales, F.A.; Lin, S.; Ahmed, S.; Zhang, Y(2021). Economic analysis and optimization of a renewable energy based power supply system with different energy storages for a remote island. Renew. 

<a name="ref1">**[11]**</a> Dutta, P.; Jaikumar, B.; Arora(2021), M.S. Applications of data envelopment analysis in supplier selection between 2000 and 2020: A literature review. Ann. Oper. Res  315, 1399–1454.

<a name="ref1">**[12]**</a> Kiritsis D., Bufardi A., Xirouchakis P(2003). Multi-criteria decision aid for product end of life options selection. IEEE international symposium on electronics and the environment; IEEE; pp. 48–53.

<a name="ref1">**[13]**</a> Sayadi M.K., Heydari M., Shahanaghi K (2009). Extension of VIKOR method for decision making problem with interval numbers. Appl Math Model. 2009;33(5):2257–2262. doi: 10.1016/j.apm.2008.06.002.

<a name="ref1">**[14]**</a> Jadidi O., Hong T.S., Firouzi F., Yusuff R.M. (2008): An Optimal Grey Based Approach Based on TOPSIS Concept for Supplier Selection Problem. “International Journal of Management Science and Engineering Management”, Vol. 4, No. 2, pp. 104-117.

<a name="ref1">**[15]**</a> Łuczak A., Wysocki F. (2006): Rozmyta wielokryterialna metoda porządkowania liniowego obiektów. Taksonomia 13, Prace Naukowe, Wydawnictwo Akademii Ekonomicznej, Wrocław, pp. 148-157.

<a name="ref1">**[16]**</a> Shih H.S., Shyur H.J., Lee E.S. (2007): An Extension of TOPSIS for Group Decision Making. “Mathematical and Computer Modelling”, Vol. 45, pp. 801-813.

---

## License


Copyright (c) 2024 decision_making

The project is license under the terms of the MIT License(MIT).
