# c17-97-t-data-bi
Demand prediction and customer behavior analysis for E-Commerce company
[![e-commerce2.jpg](https://i.postimg.cc/prL8q2f0/e-commerce2.jpg)](https://postimg.cc/BLRXvfwD)

- [Summary](#summary)
- [Results](#results)
- [Reference](#reference)
- [License](#license)

## Summary
Needs to be solved for a company in the development stage:

**Demand prediction**

Optimize inventory and production, avoid stock shortages and surpluses, and improve product turnover.

**Customer behavior analysis**

Understand customer preferences and buying habits, better understand customers, segment them, and personalize experiences.

**Advantages:**

- [x]  They share the same dataset.
- [x]  Demand prediction can identify which products are more popular and when there is likely to be an increase in demand. Customer behavior analysis can help understand why customers buy certain products and what factors influence their purchasing decisions.
- [x]  More informed decisions can be made about production, inventory, marketing strategies, and customer service.

## Installation guide

Please read [install.md](install.md) for details on how to set up this project.

## Project Organization

    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so e_commerce_project can be imported.
    │
    └── e_commerce_project               <- Source code for use in this project.
        ├── __init__.py    <- Makes e_commerce_project a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py

## Results 

## Reference

## License

It is released under the MIT license. See the [LICENSE](/LICENSE) file for details.