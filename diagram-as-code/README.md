# Introduction

Explore the diagram-as-code implementation [diagrams][1] and high level tools such as reverse
engeering tools like [clouddiscovery][2], [KubeDiagrams][3]

## Reproduce the official examples of diagrams

The following Python programs reproduce the official examples.

- three-tier-web.py
- k8s-3-replica.py
- gcp.py
- event.py
- rabbitmq.py
- on-prem-web.py
- k8s-stateful.py
- on-prem-web-colored.py

## Convert diagrams output to LaTeX

Attempt 1: First instruct diagrams to output graphviz dot format, then use dot2tex to convert into
LaTeX.

Install dot2tex:

    source .venv/bin/activate
    uv pip install dot2tex

    python on-prem-web-dot.py
    dot2tex on-prem.dot

dot2tex doesn't support images.

Attempt 2: First instruct diagrams to output SVG format, then use [svg2tikz][5] to generate to
convert into LaTeX.

Install svg2tikz:

    source .venv/bin/activate
    uv pip install svg2tikz
    python on-prem-web-svg.py
    svg2tikz --ouput on-prem.tex on-prem.svg

This method doesn't produce high-fidelity Tikz drawing either.

## Generate diagram for AWS VPC using clouddiscovery

Install the clouddiscovery package:

    source .venv/bin/activate
    uv install clouddiscovery

Run diagram generation for AWS VPC:

    cloudiscovery aws-vpc \
        --vpc-id vpc-xxxxxxx \
        --region-name xx-xxxx-xxx \
        --profile-name profile \
        --diagram yes

It generates files under the asset directory which includes an HTML table and a draw.io diagram.

## Generate diagram for Kubernetes cluster using KubeDiagrams

[KubeDiagrams][3] is a reverse engeering tool that is capable of generating Kubernetes architecture
diagrams from Kubernetes manifest files, kustomization files, Helm charts, helmfile descriptors, and
actual cluster state. The [Visualizing Cloud-native Applications with KubeDiagrams][4] is an
in-depth introduction of this tool.


[1]: https://github.com/mingrammer/diagrams
[2]: https://github.com/Cloud-Architects/cloudiscovery
[3]: https://github.com/philippemerle/KubeDiagrams
[4]: https://arxiv.org/html/2505.22879v1
[5]: https://github.com/xyz2tex/svg2tikz
