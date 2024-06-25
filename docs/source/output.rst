Damage functions
===============

FUND v.3.8
----------

A.1 : Total agriculture impact
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   A_{t,r}=A_{t,r}^{r}+A_{t,r}^{l}+A_{t,r}^{f} 

Input variables:

- Damage in agricultural production
- Damage in agricultural production level 
- Damage in agricultural production due to CO2 fertilisation

Output variables:

- Total agriculture impact


A.2 : Agriculture impact of the rate of climate change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   A_{t,r}^{r}=\alpha_{r}\left(\frac{\Delta T_{t}}{0.04}\right)^{\beta}+\left(1-\frac{1}{\rho}\right)A_{t-1,r}^{r} 

Input variables:

- Time
- Region
- Change in regional mean temperature
- Parameter for impact of climate change on economic welfare 
- Non-linearity parameter
- Speed of adaptation parameter

Output variables:

- Damage in agricultural production


A.3 : Agriculture impact of the level of climate change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   A_{t,r}^{l}\,=\,\delta_{r}^{l}T_{t}\,+\,\delta_{r}^{2}T_{t}^{2} 

Input variables:

- Time
- Region
- Change in regional mean temperature
- Parameter related to warming of 2.5°C 
- Parameter related to warming of 3.2°C 

Output variables:

- Damage in agricultural production level 


A.4 : Agriculture impact of fertilisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   A_{t,r}^{f}=\nu_{r}\ln\frac{G O2_{t}}{275}\,, 

Input variables:

- Time
- Region
- Pre-industrial concentration of CO2
- Atmospheric CO2 concentrations 
- Parameter related to CO2 fertilisation

Output variables:

- Damage in agricultural production due to CO2 fertilisation


A.5 : Agriculture production relative loss
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \frac{G A P_{t,r}}{Y_{t,r}}=\frac{G A P_{1990,r}}{Y_{1990,r}}\biggl(\frac{y_{1990,r}}{y_{t,r}}\biggr)^{2} 

Input variables:

- Gross agricultural product
- GDP in region r at time t 
- Gross domestic product per capita
- Time
- Region
- Income elasticity parameter

Output variables:

F.1 : Forestry impact
~~~~~~~~~~~~~~~~~~

.. math:: 

   F_{t,r}=\alpha_{r}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{s}\left(0.5\left(\frac{T_{t}}{1.0}\right)^{\beta}+0.5\gamma\ln\left(\frac{C O_{2,t}}{275}\right)\right) 

Input variables:

- Time
- Region
- Gross domestic product per capita
- Global mean temperature 
- Parameter for impact of climate change on economic welfare 
- Income elasticity parameter 
- Expert guess parameter 
- Parameter for the effect of doubling atmospheric CO2 concentration on forest value 

Output variables:

- Change in forestry consumer and producer surplus 


W.1 : Water resources impact
~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   W_{t,r}=\operatorname*{min}\left\{\alpha_{r}Y_{1990,r}(1-\tau)^{\prime-2000}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\not p}\left(\frac{P_{t,r}}{J_{1990,r}}\right)^{\not p}\left(\frac{T_{t}}{1.0}\right)^{\gamma}\frac{Y_{t,r}}{1.0}\right\} 

Input variables:

- Time
- Region
- Gross domestic product per capita
- Population in region r at time t 
- Global mean temperature 
- Parameter for benchmark impact 
- Parameter for economic growth response 
- Parameter for population growth response 
- Parameter for impact response to warming 
- Parameter for technological progress 

Output variables:

- Change in water resources 


E.1 : Space heating impact
~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   B_{t}=\operatorname*{max}\left\{\frac{B_{0}}{100},B_{t-}\left(1-\rho-\gamma\frac{\Delta T^{2}}{\tau^{2}}\right)\right\} 

Input variables:

- Time
- Region
- GDP in region r at time t 
- Change in regional mean temperature
- Gross domestic product per capita
- Population in region r at time t 
- Parameter for benchmark impact 
- Income elasticity of space heating demand 
- Autonomous Energy Efficiency Improvement 

Output variables:

- Decrease in expenditure on space heating 


E.2 : Space cooling impact
~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   S C_{t,r}=\alpha_{r}Y_{1990,r}\left(\frac{T_{t}}{1.0}\right)^{\beta}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\epsilon}\left(\frac{P_{t,r}}{P_{11990,r}}\right)\right/\prod_{s=1,900}^{t}4E E I_{s,r} 

Input variables:

- Time
- Region
- GDP in region r at time t 
- Change in regional mean temperature
- Gross domestic product per capita
- Population in region r at time t 
- Parameter for economic growth response 
- Income elasticity of space heating demand 
- Autonomous Energy Efficiency Improvement 

Output variables:

- Increase in expenditure on space cooling 


SLR.1 : Potential cumulative dryland impact
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \overline{{{C D}}}_{t,r}=\operatorname*{min}[\delta_{r}s_{t}^{\gamma_{r}},\zeta_{r}] 

Input variables:

- Time
- Region
- Dryland loss due to one metre sea level rise 
- Sea level rise above pre-industrial levels 
- Parameter calibrated to a digital elevation model 
- Maximum dryland loss in region 

Output variables:

SLR.2 : Potential dryland loss without protection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \overline{{{D}}}_{t,r}=\overline{{{C D}}}_{t,r}-C D_{t-1,r} 

Input variables:

- Potential cumulative dryland loss without protection 
- Actual cumulative dryland loss 

Output variables:

- Potential dryland loss without protection 


SLR.3 : Actual dryland loss in the current year
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   D_{t,r}=\left(1-P_{t,r}\right)\overline{{{D}}}_{t,r} 

Input variables:

- Fraction of the coastline protected 
- Potential dryland loss without protection 

Output variables:

- Dryland loss in year 


SLR.4 : Actual cumulative dryland loss
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   {\cal C}D_{t,r}=C D_{t-1,r}+D_{t,r} 

Input variables:

- Actual cumulative dryland loss 
- Dryland loss in year 

Output variables:

- Actual cumulative dryland loss 


SLR.5 : Value of dryland
~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   V D_{t,r}=\varphi\!\left({\frac{Y_{t,r}/A_{t,r}}{Y A_{0}}}\right)^{\!\!6} 

Input variables:

- Time
- Region
- Unit value of dryland 
- GDP in region r at time t 
- Area 
- Parameter 
- Normalisation constant 
- Income density 

Output variables:

- Unit value of dryland 


SLR.6 : Wetland loss
~~~~~~~~~~~~~~~~~

.. math:: 

   \widehat{\mathcal{W}_{t,r^{\prime}}}\longrightarrow C\mathcal{O}_{r^{\prime}}^{S}\triangle\mathsf{A}_{t}\dots C\mathcal{O}_{r^{\prime}}^{M}\mathcal{D}_{t,r^{\prime}}\triangle\mathsf{A}_{t} 

Input variables:

- Time
- Region
- Fraction of coast protected against sea level rise 
- Sea level rise above pre-industrial levels 
- Parameter for annual unit wetland loss due to sea level rise 
- Parameter for annual unit wetland loss due to coastal squeeze 

Output variables:

- Wetland loss at time 


SLR.7 : Cumulative wetland loss
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   {\mathcal W}_{t,r}^{C}\ --\left.\mathrm{Im}^{*}\!\right.\left(\left.{\mathcal W}_{t-1,r}^{C}\right.\rightarrow\mathcal W\right._{t-1,r}^{}\left.\!-\frac{}{}_{,r}\right.\mathcal W\right._{r}^{}\frac{\lambda}{\sqrt{}_{r}^{}}\right) 

Input variables:

- Cumulative wetland loss 
- Total amount of wetland exposed to sea level rise 
- Wetland loss at time 

Output variables:

- Cumulative wetland loss at time 


SLR.8 : Wetland value
~~~~~~~~~~~~~~~~~~

.. math:: 

   V W_{t,r}=\alpha\left(\frac{y_{t,r}}{y_{0}}\right)^{\beta}\left(\frac{d_{t,r}}{d_{0}}\right)^{\gamma}\left(\frac{W_{1990,r}-W_{t,r}^{C}}{W_{1990,r}}\right)^{\delta} 

Input variables:

- Time
- Region
- Gross domestic product per capita
- Population density 
- Cumulative wetland loss at time 
- Total amount of wetlands in 1990 
- Income elasticity of wetland value 
- Normalisation constant 
- Normalisation constant 
- Population density elasticity of wetland value 
- Size elasticity of wetland value 

Output variables:

- Wetland value at time 


SLR.9 : Level of protection
~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   P_{t,r}=\operatorname*{max}\left\{0,1-\frac{1}{2}\left(\frac{\mathrm{NPV}V P_{t,r}+\mathrm{NPV}V W_{t,r}}{\mathrm{NPV}V D_{t,r}}\right)\right\} 

Input variables:

- Net present value of protection if whole coast is protected 
- Net present value of the wetlands lost due to full coastal protection 
- Net present value of land lost without any coastal protection 
- Net present value of wetland lost due to coastal squeeze if whole coast is protected 

Output variables:

- Fraction of coastline to be protected 


SLR.10 : Net present cost of protection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \mathrm{NPV}{\cal P}_{t,r}=\sum_{s=t}^{\circ}\Biggl(\frac{1}{1+\rho+\eta g_{t,r}}\Biggr)^{s-t}\pi_{r}\Delta S_{t}=\frac{1+\rho+\eta g_{t,r}}{\rho+\eta g_{t,r}}\pi_{r}\Delta S_{t,s} 

Input variables:

- Time
- Region
- Annual unit cost of coastal protection 
- Sea level rise above pre-industrial levels 
- Growth rate of per capita income 
- Rate of pure time preference 
- Consumption elasticity of marginal utility 

Output variables:

- Net present costs of coastal protection at time 


SLR.11 : Net present cost of wetland loss
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \left.N P V V W_{t,r}=\sum_{s=t}^{r}W_{t,r}V W_{s,r}\left(\frac{1}{1+\rho+\eta g_{t,r}}\right)^{s-t}= 

Input variables:

- Time
- Region
- Annual unit wetland loss due to full coastal protection 
- Sea level rise above pre-industrial levels 
- Growth rate of per capita income 
- Population growth rate 
- Growth rate of wetland 
- Rate of pure time preference 
- Consumption elasticity of marginal utility 
- Income elasticity of wetland value 
- Population density elasticity of wetland value 
- Size elasticity of wetland value 

Output variables:

- Net present value of wetland loss at time 


SLR.12 : Net present cost of dryland loss
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   {\mathrm{NPV}}U_{t,r}=\sum_{s=t}^{\infty}{\overline{{D}}}_{t,r}V D_{t,r}\left({\frac{1+\epsilon d_{t,r}}{1+\rho+\eta g_{t,r}}}\right)^{s-t}={\overline{{D}}}_{t,r}V D_{t,r}{\frac{1+\rho+\eta g_{t,r}}{\rho+\eta g_{t,r}-\epsilon d_{t,r}}}\ . 

Input variables:

- Time
- Region
- Current dryland loss without protection at time 
- Current dryland value 
- Growth rate of per capita income 
- Rate of pure time preference 
- Consumption elasticity of marginal utility 
- Income elasticity of dryland value 
-  Current income density growth rate 

Output variables:

- Net present value of dryland loss at time 


E.1 : Ecosystem loss
~~~~~~~~~~~~~~~~~

.. math:: 

   E_{t,r}=\alpha P_{t,r}{\frac{y_{t,}^{\prime}{\cal Y}_{y}^{b}}{1+{\bf y}_{t,r}{\cal Y}_{y,r}}}{\frac{\Delta{\cal T}_{r}}{1+{\bf\bar{\Delta}}{2}{\cal Y}_{\tau}^{\prime}}}\bigg(1-\sigma+\sigma{\frac{B_{0}}{B_{t}^{\prime}}}\bigg) 

Input variables:

- Time
- Region
- Gross domestic product per capita
- Population in region r at time t 
- Change in regional mean temperature 
- Number of species 
- Parameter 
- Parameter 
- Parameter 
- Parameter for number of species 

Output variables:

- Value of the loss of ecosystems at time 


E.2 : Number of species
~~~~~~~~~~~~~~~~~~~~

.. math:: 

   S H_{t,r}=\alpha_{r}Y_{1990,r}\frac{\mathrm{atan}\,T_{t}}{\mathrm{atan}\,1.0}\biggl(\frac{y_{t,r}}{y_{1990,r}}\biggr)^{\epsilon}\biggl(\frac{P_{t,r}}{P_{1990,r}}\biggr)^{\epsilon}\biggl\langle\prod_{s=19900}^{t}\biggr\}^{\epsilon}\frac{\ln^{2}{\pi^{2}\pi^{2}\pi^{2}\pi^{2}\pi^{2}\pi^{2}\rangle_{t}}\,\biggl(\frac{y_{t,r}}{p_{t}-\epsilon_{r}^{2}\sqrt{2\pi_{t}\pi_{t}}^{2}\biggr)^{2}}{\epsilon_{t}^{2}-\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}-\biggl)_{t}^{2}}_{t}\,{\epsilon_{t}{t}{t}{\mu}}\,\biggr)\,\,\rho_{\biggr)\,\,\frac{t}\,\biggl(\biggr 

Input variables:

- Number of species 
- Parameter 
- Parameter 
- Change in regional mean temperature 

Output variables:

- Number of species 


HD.1 : Human health : diarrhoea
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   D_{t,r}^{d}=\mathcal{A}_{r}^{d}P_{t,r}\left(\frac{\mathcal{V}_{t,r}}{\mathcal{V}_{1990,r}}\right)^{s}\left(\frac{T_{t,r}}{\mathcal{V}_{p r e-i n d u s t r i a l,r}}\right)^{p} 

Input variables:

- Region
- Population in region r at time t 
- Time
- Gross domestic product per capita
- Regional mean temperature in degrees Celsius 
- Rate of mortality from diarrhoea in 2000 in region r 
- Income elasticity of diarrhoea mortality 
- Parameter for non-linearity of response of diarrhoea mortality to regional warming 

Output variables:

- Number of additional diarrhoea deaths 


HV : Human health : vector-borne diseases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   D_{t,r}^{\nu}=D_{1990,r}^{\nu}Q_{r}^{\nu}\left(T_{t}-T_{1990}\right)^{\beta}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\gamma} 

Input variables:

- Climate-change-induced mortality due to disease c in region r at time t 
- Mortality from vector-borne diseases in 1990 in region r 
- Time
- Region
- Vector borne disease
- Parameter indicating benchmark impact of climate change on vector-borne diseases 
- Regional mean temperature in degrees Celsius 
- Gross domestic product per capita
- Change in regional mean temperature
- Parameter for degree of non-linearity of mortality in warming 
- Income elasticity of vector-borne mortality 

Output variables:

- Number of additional deaths from vector-borne diseases 


HC.1 : Human health : cardiovascular and respiratory mortality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   {\cal D}^{c}=\varrho^{c}+\beta^{c}{\cal I}_{\cal B} 

Input variables:

- Index for the disease 
- Current temperature of the hottest or coldest month in the country 

Output variables:

- Change in mortality due to one degree global warming 


HC.2 : Human health : regional cardiovascular mortality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   D_{t,r}^{c}=\alpha_{r}^{c}T_{t}^{2}+\beta_{r}^{c}T_{t}^{2} 

Input variables:

- Region
- Time
- Change in regional mean temperature

Output variables:

- Climate-change-induced mortality due to disease c in region r at time t 


HC.3 : Human health : heat-related mortality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   U_{t,r}=\frac{\alpha\sqrt{y_{t,r}}+\beta\sqrt{P D_{t,r}}}{1+\alpha\sqrt{y_{t,r}}+\beta\sqrt{P D_{t,r}}} 

Input variables:

- Gross domestic product per capita
- Population density 
- Time
- Region

Output variables:

- Fraction of people living in cities 


TS.1 : Extreme weather : tropical storms damage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   T D_{t,r}=\sigma_{r}Y_{t,r}\left(\frac{\vartheta_{t,r}}{\vartheta_{1990,r}}\right)\left[\left(1+\rlap{\textstyle{\mathcal{D}}}{\mathcal{D}}_{t,r}\right)^{\gamma}-1\right] 

Input variables:

- Time
- Region
- GDP in region r at time t 
- Current damage as a fraction of GDP 
- Gross domestic product per capita
- Income elasticity of storm damage 
- Parameter indicating how much wind speed increases per degree warming 
- Change in regional mean temperature
- Parameter for the power of the wind in the cube of its speed 

Output variables:

- Damage due to tropical storms in region r at time t 


TS.2 : Extreme weather : tropical storm mortality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   T M_{t,r}=\beta_{r}P_{t,r}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\eta}\left[\left(1+\rlap/\partial T_{t,r}\right)^{\gamma}-1\right] 

Input variables:

- Time
- Region
- Population in region r at time t 
- Current mortality as a fraction of population 
- Gross domestic product per capita
- Parameter indicating how much wind speed increases per degree warming 
- Change in regional mean temperature
- Parameter for the power of the wind in the cube of its speed 
- Income elasticity of storm damage 

Output variables:

- Mortality due to tropical storms in region r at time t 


ETS.1 : Extratropical storms damage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   {\cal E}T\!D_{t,r}={\cal Q}_{r}Y_{t,r}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\varepsilon}\left[\left(\frac{C_{C O2,t}}{C_{C O2,p r e}}\right)^{\gamma}-1\right] 

Input variables:

- GDP in region r at time t 
- Benchmark damage from extratropical cyclones for region r 
- Gross domestic product per capita
- Income elasticity of extratropical storm damages 
- Storm sensitivity to atmospheric CO2 concentrations for region r 
- Atmospheric CO2 concentrations 
- Pre-industrial concentration of CO2

Output variables:

- Damage from extratropical cyclones at time t in region r 


ETS.2 : Extratropical storms mortality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   E T M_{t,r}=\beta_{r}{\cal P}_{t,r}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\varphi}\widehat{\cal O}_{r}\left[\left(\frac{C_{C O2,t}}{C_{C O2,p r e}}\right)^{\gamma}-1\right] 

Input variables:

- Population in region r at time t 
- Benchmark mortality from extratropical cyclones for region r 
- Gross domestic product per capita
- Income elasticity of extratropical storm mortality 
- Storm sensitivity to atmospheric CO2 concentrations for region r 
- Atmospheric CO2 concentrations 
- Pre-industrial concentration of CO2

Output variables:

- Mortality from extratropical cyclones at time t in region r 


MM.1 : Value of a statistical life
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   V S L_{t,r}=\alpha\left(\frac{y_{t,r}}{y_{0}}\right)^{6} 

Input variables:

- Income elasticity of the value of a statistical life 
- Gross domestic product per capita
- Normalisation constant 

Output variables:

- Value of a statistical life at time t in region r 


MM.2 : Value of a year of morbidity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   V M_{t,r}=\beta\left(\frac{y_{t,r}}{y_{0}}\right) 

Input variables:

- Gross domestic product per capita
- Income elasticity of the value of a year of morbidity 

Output variables:

- Value of a year of morbidity at time t in region r 


DICE 2023
---------

5 : Damage function
~~~~~~~~~~~~~~~~

.. math:: 

   \begin{array}{l l}{{\ }}&{{\displaystyle=\psi_{1}T_{A T}(t)+\psi_{2}[T_{A T}(t)]^{2}}}\\ {{}}&{{=[0.0]T_{A T}(t)+[0.003467][T_{A T}(t)]^{2}}}\end{array} 

Input variables:

- ??1 (psi 1) 
- ??2 (psi 2) 
- ?? (T) 

Output variables:

- ?? (omega) 


6 : Abatement costs
~~~~~~~~~~~~~~~~

.. math:: 

   \begin{array}{l}{{\Lambda({\bf t})\;=\;\theta_{1}(t)\mu(t)^{\theta_{2}}}}\\ {{\theta_{1}(0)\;=\;0.109062}}\\ {{\theta_{2}=\;2.6}}\end{array} 

Input variables:

- ?? (mu) 
- ??1 (theta 1) 
- ??2 (theta 2) 

Output variables:

- ? (lambda) 


PAGE02
------

22 : Tolerable rate of change
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   T R_{d,r}=\ T R_{d,0}\cdot\ T M_{r} 

Input variables:

-  Tolerable rate of change 
-  Tolerable regional multiplier 

Output variables:

-  Tolerable rate of change 


23 : Tolerable plateau
~~~~~~~~~~~~~~~~~~~

.. math:: 

   T P_{d,r}\underline{{{\Sigma}}}\underline{{{\Sigma}}}\underline{{{P}}}_{d,0}\cdot\ I=0\L_{r} 

Input variables:

-  Tolerable plateau 
-  Tolerable regional multiplier 

Output variables:

-  Tolerable plateau 


24 : Adjusted tolerable plateau
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   A^{\prime}T P_{i,d,r}\underline{{{\bf\Lambda}}}\underline{{{\bf\Lambda}}}\underline{{{\bf\Lambda}}}\underline{{{\Lambda}}}\underline{{{\Lambda}}}\lambda\alpha^{\prime}\underline{{{\cal\Psi}}}_{i,d,r} 

Input variables:

- Plateau nonegative factors characteristic to an adaptive policy
-  Tolerable plateau 

Output variables:

-  Adjusted tolerable plateau 


25 : Adjusted tolerable rate
~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   A I I\!R_{i,d,r}\underline{{{\longrightarrow}}}\ D\mathsf{)}_{d,r}\i\!\!\slash\k\mathsf{P}_{1,d,r} 

Input variables:

-  Tolerable rate of change 
- Slope nonegative factors characteristic to an adaptive policy

Output variables:

-  Adjusted tolerable rate 


26 : Adjusted tolerable level
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   {\cal L}_{i,d,r}\,=\,\mathrm{In}\mathrm{ax}\left[0,R T_{i,r}\,-\,A\,T L_{i,d,r}\right] 

Input variables:

-  Adjusted tolerable plateau 
-  Adjusted tolerable rate 
-  Adjusted tolerable level 
- GDP in region r at time t 

Output variables:

-  Adjusted tolerable level 


26 : Impact
~~~~~~~~

.. math:: 

   A T L_{i,d,r}=\operatorname*{min}\left[A T P_{i,d,t},A T L_{i-1,d,r}+A T R_{d,r}\cdot(Y_{i}-Y_{i-1})\right]\frac{array}{a,d,r}{a,r}=\sum_{i=1}^{M}\frac{a}{a,r}>0^{2}. 

Input variables:

- Regional mean temperature in degrees Celsius 
-  Adjusted tolerable level 

Output variables:

-  Regional impact of global warming 


27 : Impact of a discontinuity
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   I D I S_{i}=\operatorname*{max}[0,\,G R T_{i}-\,T D I S] 

Input variables:

- Global mean temperature 
- Temperature discontinuity

Output variables:

-  Discontinuity impact 


29 : Weighting of the impacts
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \bar{W}_{d,r}\implies\bar{W}_{d,0}\cdot\frac{W F_{r}}{100} 

Input variables:

-  Weights for monetizing impacts 
-  Regional multiplier weights

Output variables:

-  Weights for monetizing impacts 


31 : Weigthed impacts
~~~~~~~~~~~~~~~~~~

.. math:: 

   W I_{i,d,r}=\left(\frac{I_{i,d,r}}{2.5}\right)^{P O W}\cdot W_{d,r}\cdot\left(1-\frac{I M P_{i,d,r}}{100}\right)\cdot G D P_{i,r} 

Input variables:

-  Power function exponent 
-  Weights for monetizing impacts 
-  Regional impact of global warming 
- GDP in region r at time t 
- Adaptative policy

Output variables:

-  Weighted impact 


32 : Certainty equivalent of the risk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   W I D I S_{i,r}=I D I S_{i}\cdot(\frac{P D I S}{100})\cdot\,W D I S_{r}\cdot G D P_{i,r} 

Input variables:

-  Discontinuity weight 
-  Discontinuity impact 
- GDP in region r at time t 

Output variables:

-  Weighted impact of discontinuity 


33 : Total weighted impact
~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   W I T_{i,r}\stackrel{_{\textstyle>}}{=}\sum_{d}W I_{i,d,r}+W I D I J J_{i,r} 

Input variables:

-  Weighted impact 
-  Weighted impact of discontinuity 

Output variables:

-  Total weighted impact 


38 : Adjusted damage
~~~~~~~~~~~~~~~~~

.. math:: 

   \ A\,L\!\!\!\!\slash\,\L_{i,r}\,\longrightarrow\,\ W\!\!\!\!\slash\,J\L^{*}\!\!\!\!\slash\,A\to\nabla\!\!\!\slash\,\L_{i}\,\longrightarrow\,\L^{*}\,\L_{}\,k\,\L_{}\,\L^{}\,\Psi=\,\L^{*}\Psi_{i}\,\L^{}\, 

Input variables:

-  Total weighted impact 
- GDP in region r at time t 

Output variables:

-  Adjusted damages 


39 : Discounted damages
~~~~~~~~~~~~~~~~~~~~

.. math:: 

   D D=\sum_{i,r}(A D_{i,r})\cdot\prod_{k=1}^{i}\left(1+d r_{k,r}\cdot\frac{r i c}{100}\right)^{-(Y_{k}-Y_{k-1})} 

Input variables:

-  Adjusted damages 
- Discount rate for impacts

Output variables:

-  Net present value of global warming impacts 


C3IAM
-----

12 : Damage function
~~~~~~~~~~~~~~~~~

.. math:: 

   D_{i}(t)=1-\frac{1}{1+a_{1,i}T_{1}(t)+a_{2,i}T_{1}(t)^{2}}, 

Input variables:

-  Climate damage fraction of gross output 

Output variables:

- Change in regional mean temperature 


GRACE
-----

3.1 : Productivity of land in agriculture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   d X=\alpha d T^{2}+\beta d T+\gamma d P 

Input variables:

- Global mean temperature 
-  Rate of change in precipitation 

Output variables:

- Productivity of land in agriculture


3.1 : Productivity of land in forestry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   d X=\alpha d T^{2}+\beta d T+\gamma d P 

Input variables:

- Global mean temperature 
-  Rate of change in precipitation 

Output variables:

- Productivity of land in forestry


3.1 : Fish stock
~~~~~~~~~~~~~

.. math:: 

   d X=\alpha d T^{2}+\beta d T+\gamma d P 

Input variables:

- Global mean temperature 
-  Rate of change in precipitation 

Output variables:

- Fish stock


3.1 : Water cooling and run-off
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   d X=\alpha d T^{2}+\beta d T+\gamma d P 

Input variables:

- Global mean temperature 
-  Rate of change in precipitation 

Output variables:

- Natural resources in thermal power


3.1 : Run-off
~~~~~~~~~~

.. math:: 

   d X=\alpha d T^{2}+\beta d T+\gamma d P 

Input variables:

- Global mean temperature 
-  Rate of change in precipitation 

Output variables:

- Natural resources in hydro power


3.1 : Energy demand
~~~~~~~~~~~~~~~~

.. math:: 

   d X=\alpha d T^{2}+\beta d T+\gamma d P 

Input variables:

- Global mean temperature 
-  Rate of change in precipitation 

Output variables:

- Energy demand


3.1 : Tourism
~~~~~~~~~~

.. math:: 

   d X=\alpha d T^{2}+\beta d T+\gamma d P 

Input variables:

- Global mean temperature 
-  Rate of change in precipitation 

Output variables:

- Final demand for transport and services


3.1 : Extreme events
~~~~~~~~~~~~~~~~~

.. math:: 

   d X=\alpha d T^{2}+\beta d T+\gamma d P 

Input variables:

- Global mean temperature 
-  Rate of change in precipitation 

Output variables:

- Real capital


3.1 : Sea-level rise
~~~~~~~~~~~~~~~~~

.. math:: 

   d X=\alpha d T^{2}+\beta d T+\gamma d P 

Input variables:

- Global mean temperature 
-  Rate of change in precipitation 

Output variables:

- Real capital


3.1 : Health
~~~~~~~~~

.. math:: 

   d X=\alpha d T^{2}+\beta d T+\gamma d P 

Input variables:

- Global mean temperature 
-  Rate of change in precipitation 

Output variables:

- Labour


WITNESS
-------

nan : Dice-like damage
~~~~~~~~~~~~~~~~~~~

.. math:: 

Input variables:

- Global mean temperature 

Output variables:

-  Climate damage fraction of gross output 


nan : Tipping point damage
~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

Input variables:

- Global mean temperature 

Output variables:

-  Abatement cost fraction of gross output 


DSK
---

A.128 : Climate shock
~~~~~~~~~~~~~~~~~~

.. math:: 

   \text{SHOCKS}~t \sim Beta(\theta_{s1,t}, \theta_{s2,t}) 

Input variables:

- Beta 1
- Beta 2

Output variables:

- Propbability of occurence of a shock


A.129 : Beta 1 parameter
~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \theta_{s1,t} = \theta_{s1,0} (1 + \ln \left( \frac{T_{empt-1}}{T_{empt0}} \right))^{\Upsilon_{s3}} 

Input variables:

- Global mean temperature 

Output variables:

- Beta 1


A.129 : Beta 2 parameter
~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \theta_{s2,t} = \theta_{s2,0} \left( \frac{T_{empt0}}{T_{empt-1}} \right)^{\Upsilon_{s4}}  

Input variables:

- Global mean temperature 

Output variables:

- Beta 2


DEFINE
------

55 : Damage function
~~~~~~~~~~~~~~~~~

.. math:: 

   \Delta T = 1 - \frac{1}{1 + \eta_1 TAT + \eta_2 TAT^2 + \eta_3 TAT} 

Input variables:

- Global mean temperature 

Output variables:

- Productivity
- Consumption
- Investment


Giraud Stock-Flow model
-----------------------

3.5 : Damage function
~~~~~~~~~~~~~~~~~~

.. math:: 

   D = 1 - \frac{1}{1 + \pi_1 T + \pi_2 T^2}  

Input variables:

- Global mean temperature 

Output variables:

- GDP in region r at time t 


