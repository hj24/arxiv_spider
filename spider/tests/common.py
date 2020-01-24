import os


single_tag = """<li class="arxiv-result">
    <div class="is-marginless">
      <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/1911.11002">arXiv:1911.11002</a>
        <span>&nbsp;[<a href="https://arxiv.org/pdf/1911.11002">pdf</a>, <a href="https://arxiv.org/format/1911.11002">other</a>]&nbsp;</span>
      </p>
      <div class="tags is-inline-block">
        <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Applications">stat.AP</span>
        
          
            <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation">stat.CO</span>
          
        </div>
      
    </div>
    
    <p class="title is-5 mathjax">
      
        ForestFit : An R package for modeling tree diameter distributions
      
    </p>
    <p class="authors">
      <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
      
      <a href="/search/?searchtype=author&amp;query=Teimouri%2C+M">Mahdi Teimouri</a>, 
      
      <a href="/search/?searchtype=author&amp;query=Doser%2C+J+W">Jeffrey W. Doser</a>, 
      
      <a href="/search/?searchtype=author&amp;query=Finley%2C+A+O">Andrew O. Finley</a>
      
    </p>
    
    <p class="abstract mathjax">
      <span class="search-hit">Abstract</span>:
      <span class="abstract-short has-text-grey-dark mathjax" id="1911.11002v1-abstract-short" style="display: inline;">
        Modeling the diameter distribution of trees in forest stands is a common <span class="search-hit mathjax">forestry</span> task that supports key biologically and economically relevant management decisions. The choice of model used to represent the diameter distribution and how to estimate its parameters has received much attention in the <span class="search-hit mathjax">forestry</span> literature;&hellip;
        <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('1911.11002v1-abstract-full').style.display = 'inline'; document.getElementById('1911.11002v1-abstract-short').style.display = 'none';">&#9661; More</a>
      </span>
      <span class="abstract-full has-text-grey-dark mathjax" id="1911.11002v1-abstract-full" style="display: none;">
        Modeling the diameter distribution of trees in forest stands is a common <span class="search-hit mathjax">forestry</span> task that supports key biologically and economically relevant management decisions. The choice of model used to represent the diameter distribution and how to estimate its parameters has received much attention in the <span class="search-hit mathjax">forestry</span> literature; however, accessible software that facilitates comprehensive comparison of the myriad modeling approaches is not available. To this end, we developed an R package called ForestFit that simplifies estimation of common probability distributions used to model tree diameter distributions, including the two- and three-parameter Weibull distributions, Johnson&#39;s SB distribution, Birnbaum-Saunders distribution, and finite mixture distributions. Frequentist and Bayesian techniques are provided for individual tree diameter data, as well as grouped data. Additional functionality facilitates fitting growth curves to height-diameter data. The package also provides a set of functions for computing probability distributions and simulating random realizations from common finite mixture models.
        <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('1911.11002v1-abstract-full').style.display = 'none'; document.getElementById('1911.11002v1-abstract-short').style.display = 'inline';">&#9651; Less</a>
      </span>
    </p>
    

    <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 25 November, 2019; 
      <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> November 2019.
      
    </p>
    
    <p class="comments is-size-7">
      <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
      <span class="has-text-grey-dark mathjax">10 pages, 7 figures</span>
    </p>   
  </li>
"""

def read_html(path):
    res = ''
    with open(path, 'r', encoding='utf-8') as fo:
        for line in fo:
            res += line
    return res

if __name__ == '__main__':
    p = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'arxiv.html')
    print(p)
    print(read_html(p))
