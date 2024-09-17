# Алгоритм вычисления двухэлектронной функции на основе одноэлектронных

## Шаг 1

Создаем каталог `without_interaction`. В этом каталоге создаем три каталога:
- `external_electron` для расчета эволюции одноэлектронной волновой функции внешнего электрона
- `inner_electron` для расчета эволюции одноэлектронной волновой функции внутреннего электрона

И клонируем репозиторий для вычисления двухэлектронной волновой функции на 
основе одноэлектронных:

```bash
git clone https://github.com/DenTyur/make_2e_favefunc_from_1e
```

В итоге должна получиться следующая стркутура каталогов:
.                                                                                              │  20                                                                                          
└── without_interaction                                                                        │  21 ▎                                                                                        
    ├── external_electron                                                                      │  22 ▎                                                                                        
    ├── inner_electron                                                                         │  23 ▎                                                                                        
    └── make_2e_wavefunc_from_1e   

## Шаг 2

Насчитываем эволюцию одноэлектронной функции внешнего электрона

### Шаг 2.1

Переходим в каталог `without_interaction/external_electron`. И клонируем в него:
```bash
git clone https://github.com/DenTyur/RSSFM1D
```
После этого появится:

```
external_electron                                                                                              │   4   Создаем файл `dir_paths.txt` в каталоге `make_2e_wavefunc_from_1e/python`.             
└── RSSFM1D                                                                                    │   5   В этот файл в три строки записываем абсолютный путь к каталогам:                       
    ├── Cargo.toml                                                                             │  6   ▏- `make_2e_wavefunc_from_1e`                                                          
    ├── README.md                                                                              │   7   ▏- `inner_electron`                                                                    
    └── src                                                                                    │   8   ▏- `external_electron`                                                                 
        ├── evolution.rs                                                                       │   9                                                                                          
        ├── field.rs                                                                           │  10                                                                                          
        ├── main.rs                                                                            │  11 ▎                                                                                        
        ├── parameters.rs                                                                      │  12 ▎                                                                                        
        ├── potentials.rs                                                                      │  13 ▎                                                                                        
        ├── python                                                                             │  14 ▎                                                                                        
        │   ├── plot_initial_arrays.ipynb                                                      │  15 ▎                                                                                        
        │   └── plot_psi_x_time_slises.py                                                      │  16 ▎                                                                                        
        └── wave_function.rs       
```

### Шаг 1

Создаем файл `dir_paths.txt` в каталоге `make_2e_wavefunc_from_1e/python`.
В этот файл в три строки записываем абсолютный путь к каталогам:
 - `make_2e_wavefunc_from_1e`
 - `inner_electron`
 - `external_electron`

























