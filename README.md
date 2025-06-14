# Dataset for C-Fitness-Tracking

This repo contains the raw data used in the optimization process of the C-Step-Counter algorithm implemented on [Hacktor Watch](https://github.com/dantudose/open-smartwatch).
The optimization was done using the script from [C-optimize-variables](https://github.com/Ana-Mirza/C-optimize-variables).

The software running on the watch can be found at [hectorwatch-nuttx](https://github.com/Ana-Mirza/hectorwatch-nuttx).

### File structure
```
$ tree -L 1
.
├── optimize
├── validate # data used for validation
├── README.md
└── text_to_csv.py # script transforming acc raw data to csv format
```
