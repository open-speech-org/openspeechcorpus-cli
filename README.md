# Open Speech Corpus CLI

This repository contains the code required to download audiodata from 
[openspeechcorpus.com](http://openspeechcorpus.contraslash.com)

Open Speech Corpus is composed by far for three subcorpuses:

- Tales: A crowdsourced corpus based on reading of latin american short tales
- Aphasia: A crowdsourced corpus based in words categorized in 4 levels of difficulty
- Isolated words: A crowdsourced corpus based in isolated words

To download files from the Tales Project use

```bash
ops  \
    --output_folder tales/ \
    --output_file tales.txt  \
    --corpus tales
```

To download files from the Isolated Words Project use

```bash
ops  \
    --output_folder isolated_words/ \
    --output_file isolated_words.txt  \
    --corpus words
```

To download files from the Aphasia Project use

```bash
ops  \
    --output_folder aphasia/ \
    --output_file aphasia.txt  \
    --corpus aphasia
```

## Parameters ussage

### `--download_all`

You can download the whole corpus using the flag `--download_all`

```bash
ops  \
    --output_folder aphasia/ \
    --output_file aphasia.txt  \
    --corpus aphasia \
    --download_all
```

### `--from` and `--to`

By default the page size is 500, to modify it use the args `--from` and `--to` i.e:

```bash
ops  \
    --from 500 \
    --to 1000 \
    --output_folder aphasia/ \
    --output_file aphasia.txt  \
    --corpus aphasia
```


If you use the flag `--download_all` with the flag `--from` the process will start in the specified arg `from` using a
page size of 500

### `--extra_query_params`

We also support an argument `--extra_query_params` which overwrites the `--from`, `--to` and `--download_all` arguments
and downloads all files in the body response, you must define the `--corpus` argument anyway

```bash
ops  \
    --output_folder aphasia/ \
    --output_file aphasia_letters.txt  \
    --corpus aphasia \
    --extra_query_params "level_sentence__id__gte=846&level_sentence__id__lte=870"
```

## Recursive Convert

The Open Speech Corpus stores its files in mp4 format, which is undesired for most audio processing tasks. To convert 
the files into a wav format, first install [ffmpeg](https://www.ffmpeg.org/download.html), then you can execute the
`recursive_convert` utility which receives as first argument the source_folder with the mp4 files and as second argument
the output folder i.e.:

```bash
recursive_convert aphasia aphasia_wav
```

## CMU Sphinx Configuration

The Open Speech Corpus also defines some scripts to generate configurations for 
[CMU Sphinx](https://cmusphinx.github.io/).
 
First initialize a project with the `sphinx_train` command

```bash
sphinxtrain -t simple_words setup
```
   
To generate a configuration use the command `configure_sphinx`, which creates the transcription, fileids, fillers and
dic files.

```bash
configure_sphinx simple_words \
    --transcription_file words.txt \
    --etc_folder simple_words/etc \
    --test_size 0.5
```

Also you need to define a language model which receives the DB_NAME and the base project folder

```bash
generate_language_model simple_words simple_words
```

To delete the configuration files use the command `clean_previous_configuration`

```bash
clean_previous_configuration simple_words --etc_folder simple_words/etc/
```

## HTK Configuration

The Open Speech Corpus also defines some scripts to train models using [HTK](http://htk.eng.cam.ac.uk/)

To generate a word grammar use 

```bash
configure_htk \
    --transcription_file words.txt \
    --project_folder htk_words \
    --wav_folder words_wav \
    htk_words
```
