# CAD to OpenUSD
<h1 align="center">
  <b>🔧 <code>CAD-to-OpenUSD</code></b>
</h1>
<p align="center">
<a href="https://docs.nvidia.com/learn-openusd/latest/index.html"><img alt="Learn Open USD" src="https://img.shields.io/static/v1?label=&message=LearnOpenUSD&color=purple&logo=Nvidia"></a>
<a href="https://github.com/nAurava-Technologies/CAD-to-OpenUSD.git"><img alt="Github Repo" src="https://img.shields.io/static/v1?label=&message=Source%20code&color=purple&logo=github"></a>
<a href="https://github.com/nAurava-Technologies/CAD-to-OpenUSD/tree/main/prod/lib/actors/nova_carter"><img alt="Github actors repo" src="https://img.shields.io/static/v1?label=&message=Examples&color=purple&logo=github"></a>
<a href="https://developer.nvidia.com/blog/building-cad-to-usd-workflows-with-nvidia-omniverse/"><img alt="Nvidia Blog" src="https://img.shields.io/static/v1?label=&message=Technical%20Blog&color=purple&logo=Nvidia"></a>
<a href="https://drive.google.com/drive/folders/14m8q_ZWU_hc3nMCTxg66reiSNl78jRxV"><img alt="Test Cases
" src="https://img.shields.io/static/v1?label=&message=Test%20Case&color=purple&logo=GoogleDrive"></a>
<a href="https://drive.google.com/drive/folders/1oDv4bdMmgy7YmxuC_LthkCnnbcPKm5t7?usp=sharing"><img alt="MOM" src="https://img.shields.io/static/v1?label=&message=MeetingMinutes&color=purple&logo=googledrive"></a>
<a href="https://discord.com/invite/nvidiaomniverse"><img alt="Discord" src="https://img.shields.io/static/v1?label=&message=Open%20USD%20Study%20Group&color=purple&logo=Discord"></a>
</p>

## Configuration

### uv
This repository uses [uv](https://docs.astral.sh/uv/) for dependency management. If you're new to uv, you don't need to know much more than the commands we use in the [build instructions](#How-to-Build). We recommend [installing uv](https://docs.astral.sh/uv/getting-started/installation/).


## Run the Converter

1. In the `./kit/`, run `./repo.bat build`
2. `uv run cad2usd`

This will convert the `nova_carter_full.step` at the root of the rop and output a USD file in the same location.

## Build Docs
1. `uv run sphinx-build -M html docs/ docs/_build/`
1. `uv run python -m http.server 8000 -d docs/_build/html/`
1. In a web browser, open `http://localhost:8000`
