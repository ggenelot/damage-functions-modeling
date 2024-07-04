Damage functions
===============

DICE 2023
---------

5 : Damage function
~~~~~~~~~~~~~~~~~~~

.. math:: 

   \begin{array}{l l}{{\ }}&{{\displaystyle=\psi_{1}T_{A T}(t)+\psi_{2}[T_{A T}(t)]^{2}}}\\ {{}}&{{=[0.0]T_{A T}(t)+[0.003467][T_{A T}(t)]^{2}}}\end{array} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.dice_5_eq_damage_function 

6 : Abatement costs
~~~~~~~~~~~~~~~~~~~

.. math:: 

   \begin{array}{l}{{\Lambda({\bf t})\;=\;\theta_{1}(t)\mu(t)^{\theta_{2}}}}\\ {{\theta_{1}(0)\;=\;0.109062}}\\ {{\theta_{2}=\;2.6}}\end{array} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.dice_6_eq_abatment_function 

DSK
---

A.128 : Climate shock
~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \text{SHOCKS}~t \sim Beta(\theta_{s1,t}, \theta_{s2,t}) 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.dsk_a128_eq_shock_from_climate_change 

FUND v.3.8
----------

A.1 : Total agriculture impact
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   A_{t,r}=A_{t,r}^{r}+A_{t,r}^{l}+A_{t,r}^{f} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_a1_eq_total_agricultural_impact 

A.2 : Agriculture impact of the rate of climate change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   A_{t,r}^{r}=\alpha_{r}\left(\frac{\Delta T_{t}}{0.04}\right)^{\beta}+\left(1-\frac{1}{\rho}\right)A_{t-1,r}^{r} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_a2_eq_agricultural_impact_of_the_rate_of_climate_change 

A.3 : Agriculture impact of the level of climate change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   A_{t,r}^{l}\,=\,\delta_{r}^{l}T_{t}\,+\,\delta_{r}^{2}T_{t}^{2} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_a3_eq_agricultural_impact_of_the_level_of_climate_change 

A.4 : Agriculture impact of fertilisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   A_{t,r}^{f}=\nu_{r}\ln\frac{G O2_{t}}{275}\,, 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_a4_eq_agricultural_imact_of_the_fertilisation 

E.1 : Space heating impact
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   B_{t}=\operatorname*{max}\left\{\frac{B_{0}}{100},B_{t-}\left(1-\rho-\gamma\frac{\Delta T^{2}}{\tau^{2}}\right)\right\} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_e1_eq_space_heating 

E.1 : Ecosystem loss
~~~~~~~~~~~~~~~~~~~~

.. math:: 

   E_{t,r}=\alpha P_{t,r}{\frac{y_{t,}^{\prime}{\cal Y}_{y}^{b}}{1+{\bf y}_{t,r}{\cal Y}_{y,r}}}{\frac{\Delta{\cal T}_{r}}{1+{\bf\bar{\Delta}}{2}{\cal Y}_{\tau}^{\prime}}}\bigg(1-\sigma+\sigma{\frac{B_{0}}{B_{t}^{\prime}}}\bigg) 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_e1_eq_space_heating 

E.1 : Space heating impact
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   B_{t}=\operatorname*{max}\left\{\frac{B_{0}}{100},B_{t-}\left(1-\rho-\gamma\frac{\Delta T^{2}}{\tau^{2}}\right)\right\} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_e1_eq_value_of_the_loss_of_the_ecosystems 

E.1 : Ecosystem loss
~~~~~~~~~~~~~~~~~~~~

.. math:: 

   E_{t,r}=\alpha P_{t,r}{\frac{y_{t,}^{\prime}{\cal Y}_{y}^{b}}{1+{\bf y}_{t,r}{\cal Y}_{y,r}}}{\frac{\Delta{\cal T}_{r}}{1+{\bf\bar{\Delta}}{2}{\cal Y}_{\tau}^{\prime}}}\bigg(1-\sigma+\sigma{\frac{B_{0}}{B_{t}^{\prime}}}\bigg) 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_e1_eq_value_of_the_loss_of_the_ecosystems 

E.2 : Space cooling impact
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   S C_{t,r}=\alpha_{r}Y_{1990,r}\left(\frac{T_{t}}{1.0}\right)^{\beta}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\epsilon}\left(\frac{P_{t,r}}{P_{11990,r}}\right)\right/\prod_{s=1,900}^{t}4E E I_{s,r} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_e2_eq_space_cooling 

E.2 : Number of species
~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   S H_{t,r}=\alpha_{r}Y_{1990,r}\frac{\mathrm{atan}\,T_{t}}{\mathrm{atan}\,1.0}\biggl(\frac{y_{t,r}}{y_{1990,r}}\biggr)^{\epsilon}\biggl(\frac{P_{t,r}}{P_{1990,r}}\biggr)^{\epsilon}\biggl\langle\prod_{s=19900}^{t}\biggr\}^{\epsilon}\frac{\ln^{2}{\pi^{2}\pi^{2}\pi^{2}\pi^{2}\pi^{2}\pi^{2}\rangle_{t}}\,\biggl(\frac{y_{t,r}}{p_{t}-\epsilon_{r}^{2}\sqrt{2\pi_{t}\pi_{t}}^{2}\biggr)^{2}}{\epsilon_{t}^{2}-\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}-\biggl)_{t}^{2}}_{t}\,{\epsilon_{t}{t}{t}{\mu}}\,\biggr)\,\,\rho_{\biggr)\,\,\frac{t}\,\biggl(\biggr 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_e2_eq_space_cooling 

E.2 : Space cooling impact
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   S C_{t,r}=\alpha_{r}Y_{1990,r}\left(\frac{T_{t}}{1.0}\right)^{\beta}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\epsilon}\left(\frac{P_{t,r}}{P_{11990,r}}\right)\right/\prod_{s=1,900}^{t}4E E I_{s,r} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_e2_eq_number_of_species 

E.2 : Number of species
~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   S H_{t,r}=\alpha_{r}Y_{1990,r}\frac{\mathrm{atan}\,T_{t}}{\mathrm{atan}\,1.0}\biggl(\frac{y_{t,r}}{y_{1990,r}}\biggr)^{\epsilon}\biggl(\frac{P_{t,r}}{P_{1990,r}}\biggr)^{\epsilon}\biggl\langle\prod_{s=19900}^{t}\biggr\}^{\epsilon}\frac{\ln^{2}{\pi^{2}\pi^{2}\pi^{2}\pi^{2}\pi^{2}\pi^{2}\rangle_{t}}\,\biggl(\frac{y_{t,r}}{p_{t}-\epsilon_{r}^{2}\sqrt{2\pi_{t}\pi_{t}}^{2}\biggr)^{2}}{\epsilon_{t}^{2}-\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}\pi_{t}^{2}-\biggl)_{t}^{2}}_{t}\,{\epsilon_{t}{t}{t}{\mu}}\,\biggr)\,\,\rho_{\biggr)\,\,\frac{t}\,\biggl(\biggr 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_e2_eq_number_of_species 

ETS.1 : Extratropical storms damage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   {\cal E}T\!D_{t,r}={\cal Q}_{r}Y_{t,r}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\varepsilon}\left[\left(\frac{C_{C O2,t}}{C_{C O2,p r e}}\right)^{\gamma}-1\right] 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_ets1_eq_extratropical_storms 

ETS.2 : Extratropical storms mortality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   E T M_{t,r}=\beta_{r}{\cal P}_{t,r}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\varphi}\widehat{\cal O}_{r}\left[\left(\frac{C_{C O2,t}}{C_{C O2,p r e}}\right)^{\gamma}-1\right] 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_ets2_eq_mortality_from_extratropical_storm 

F.1 : Forestry impact
~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   F_{t,r}=\alpha_{r}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{s}\left(0.5\left(\frac{T_{t}}{1.0}\right)^{\beta}+0.5\gamma\ln\left(\frac{C O_{2,t}}{275}\right)\right) 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_f1_eq_forestry_change_in_consumer_and_producer_surplus 

HD.1 : Human health : diarrhoea
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   D_{t,r}^{d}=\mathcal{A}_{r}^{d}P_{t,r}\left(\frac{\mathcal{V}_{t,r}}{\mathcal{V}_{1990,r}}\right)^{s}\left(\frac{T_{t,r}}{\mathcal{V}_{p r e-i n d u s t r i a l,r}}\right)^{p} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_hd1_eq_additional_diarrhoea_deaths 

HV : Human health : vector-borne diseases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   D_{t,r}^{\nu}=D_{1990,r}^{\nu}Q_{r}^{\nu}\left(T_{t}-T_{1990}\right)^{\beta}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\gamma} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_hv_eq_vectorborn_diseases 

MM.1 : Value of a statistical life
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   V S L_{t,r}=\alpha\left(\frac{y_{t,r}}{y_{0}}\right)^{6} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_mm1_eq_value_of_a_statistical_life 

MM.2 : Value of a year of morbidity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   V M_{t,r}=\beta\left(\frac{y_{t,r}}{y_{0}}\right) 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_mm2_eq_value_of_a_year_of_morbidity 

SLR.10 : Net present cost of protection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \mathrm{NPV}{\cal P}_{t,r}=\sum_{s=t}^{\circ}\Biggl(\frac{1}{1+\rho+\eta g_{t,r}}\Biggr)^{s-t}\pi_{r}\Delta S_{t}=\frac{1+\rho+\eta g_{t,r}}{\rho+\eta g_{t,r}}\pi_{r}\Delta S_{t,s} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr10_eq_npvvp 

SLR.11 : Net present cost of wetland loss
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \left.N P V V W_{t,r}=\sum_{s=t}^{r}W_{t,r}V W_{s,r}\left(\frac{1}{1+\rho+\eta g_{t,r}}\right)^{s-t}= 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr11_eq_npvvw 

SLR.12 : Net present cost of dryland loss
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   {\mathrm{NPV}}U_{t,r}=\sum_{s=t}^{\infty}{\overline{{D}}}_{t,r}V D_{t,r}\left({\frac{1+\epsilon d_{t,r}}{1+\rho+\eta g_{t,r}}}\right)^{s-t}={\overline{{D}}}_{t,r}V D_{t,r}{\frac{1+\rho+\eta g_{t,r}}{\rho+\eta g_{t,r}-\epsilon d_{t,r}}}\ . 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr12_eq_npvvd 

SLR.1 : Potential cumulative dryland impact
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \overline{{{C D}}}_{t,r}=\operatorname*{min}[\delta_{r}s_{t}^{\gamma_{r}},\zeta_{r}] 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr1_eq_slr_dryland_loss 

SLR.2 : Potential dryland loss without protection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \overline{{{D}}}_{t,r}=\overline{{{C D}}}_{t,r}-C D_{t-1,r} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr2_eq_potential_dryland_loss 

SLR.3 : Actual dryland loss in the current year
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   D_{t,r}=\left(1-P_{t,r}\right)\overline{{{D}}}_{t,r} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr3_eq_actual_dryland_loss 

SLR.4 : Actual cumulative dryland loss
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   {\cal C}D_{t,r}=C D_{t-1,r}+D_{t,r} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr4_eq_actual_cumulative_dryland_lost 

SLR.5 : Value of dryland
~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   V D_{t,r}=\varphi\!\left({\frac{Y_{t,r}/A_{t,r}}{Y A_{0}}}\right)^{\!\!6} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr5_eq_dryland_value 

SLR.6 : Wetland loss
~~~~~~~~~~~~~~~~~~~~

.. math:: 

   \widehat{\mathcal{W}_{t,r^{\prime}}}\longrightarrow C\mathcal{O}_{r^{\prime}}^{S}\triangle\mathsf{A}_{t}\dots C\mathcal{O}_{r^{\prime}}^{M}\mathcal{D}_{t,r^{\prime}}\triangle\mathsf{A}_{t} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr6_eq_wetland_loss 

SLR.7 : Cumulative wetland loss
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   {\mathcal W}_{t,r}^{C}\ --\left.\mathrm{Im}^{*}\!\right.\left(\left.{\mathcal W}_{t-1,r}^{C}\right.\rightarrow\mathcal W\right._{t-1,r}^{}\left.\!-\frac{}{}_{,r}\right.\mathcal W\right._{r}^{}\frac{\lambda}{\sqrt{}_{r}^{}}\right) 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr7_eq_cumulative_wetland_loss 

SLR.8 : Wetland value
~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   V W_{t,r}=\alpha\left(\frac{y_{t,r}}{y_{0}}\right)^{\beta}\left(\frac{d_{t,r}}{d_{0}}\right)^{\gamma}\left(\frac{W_{1990,r}-W_{t,r}^{C}}{W_{1990,r}}\right)^{\delta} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_slr8_eq_wetland_value 

TS.1 : Extreme weather : tropical storms damage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   T D_{t,r}=\sigma_{r}Y_{t,r}\left(\frac{\vartheta_{t,r}}{\vartheta_{1990,r}}\right)\left[\left(1+\rlap{\textstyle{\mathcal{D}}}{\mathcal{D}}_{t,r}\right)^{\gamma}-1\right] 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_ts1_eq_tropical_storms_damages 

TS.2 : Extreme weather : tropical storm mortality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   T M_{t,r}=\beta_{r}P_{t,r}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\eta}\left[\left(1+\rlap/\partial T_{t,r}\right)^{\gamma}-1\right] 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_ts2_eq_tropical_storms_mortality 

W.1 : Water resources impact
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: 

   W_{t,r}=\operatorname*{min}\left\{\alpha_{r}Y_{1990,r}(1-\tau)^{\prime-2000}\left(\frac{y_{t,r}}{y_{1990,r}}\right)^{\not p}\left(\frac{P_{t,r}}{J_{1990,r}}\right)^{\not p}\left(\frac{T_{t}}{1.0}\right)^{\gamma}\frac{Y_{t,r}}{1.0}\right\} 

Input variables:


Output variables:

.. autofunction:: WILIAM.WILIAM.fund_w1_eq_change_in_water_resources 

