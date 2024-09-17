# Алгоритм вычисления двухэлектронной функции на основе одноэлектронных

## Шаг 1

Создаем каталог `without_interaction`. В этом каталоге создаем три каталога:
- `external_electron` для расчета эволюции одноэлектронной волновой функции внешнего электрона
- `inner_electron` для расчета эволюции одноэлектронной волновой функции внутреннего электрона

```bash
mkdir without_interaction
cd without_interaction
mkdir external_electron
mkdir inner_electron
```
И клонируем репозиторий для вычисления двухэлектронной волновой функции на 
основе одноэлектронных:

```bash
git clone https://github.com/DenTyur/make_2e_favefunc_from_1e
```

В итоге должна получиться следующая стркутура каталогов:
```
.                                                                                              │  20                                                                                          
└── without_interaction                                                                        │  21 ▎                                                                                        
    ├── external_electron                                                                      │  22 ▎                                                                                        
    ├── inner_electron                                                                         │  23 ▎                                                                                        
    └── make_2e_wavefunc_from_1e   
```

## Шаг 2

Насчитываем эволюцию одноэлектронной функции внешнего электрона

### Шаг 2.1

Переходим в каталог `without_interaction/external_electron`. И клонируем в него:

```bash
cd external_electron
```

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

### Шаг 2.2

Создаем каталог `external_electron/RSSFM1D/src/arrays_saved`:
```bash
mkdir RSSFM1D/src/arrays_saved
```
И кладем в этот каталог заранее насчитанные:
- `x.npy` (массив координатной сетки)
- `psi_initial.npy` (комплексный массив волновой функции)
- `atomic_potential.npy` (комплексный массив атомного потенциала
                        ВМЕСТЕ с поглощающим слоем!)
                        
**Если эти массивы лежат в других каталогах, то указать полные пути к ним в `src/main.rs`**

Можно построить графики этих начальных массивов в 
```
external_electron/RSSFM1D/src/python/plot_initial_arrays.ipynb
```

### Шаг 2.3

Задаем в `external_electron/RSSFM1D/src/main.rs` временную сетку. Например:
```rust
let mut t = Tspace::new(0., 0.2, 200, 31);
```
где `Tspace::new(t0: f64, dt: f64, n_steps: usize, nt: usize)`

### Шаг 2.4

Задаем внешнее электрическое поле в файле `/src/field.rs` и инициализируем его в `/src/main.rs`.
Например:
`/src/main.rs`
```rust
let field1d = Field1D {
    amplitude: 0.035,
    omega: 0.04,
    x_envelop: 50.0001,
};
```

### Шаг 2.5

Запускаем расчет эволюции волновой функции. Из директории
`external_electron/RSSFM1D/src`:
```bash
cargo run --release
```
После этого появятся:
- `/src/arrays_saved/time_evol/t.npy` - массив временной сетки
- `/src/arrays_saved/time_evol/psi_x` - каталог с массивами временных срезов волновой функции
Эти срезы согласованы с массивом временной сетки

Можно построить графики временных срезов волновой функции, запустив
```bash
cd RSSFM1D/src/python 
python 3 plot_psi_x_time_slises.py
```
После этого появится каталог `RSSFM1D/src/imgs/time_evol/psi_x` в графиками временных врезов волновой фукции

<!-- ### Шаг 1 -->
<!---->
<!-- Создаем файл `dir_paths.txt` в каталоге `make_2e_wavefunc_from_1e/python`. -->
<!-- В этот файл в три строки записываем абсолютный путь к каталогам: -->
<!--  - `make_2e_wavefunc_from_1e` -->
<!--  - `inner_electron` -->
<!--  - `external_electron` -->

























