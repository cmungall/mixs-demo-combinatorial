# Auto generated from mixs.linkml.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-25 15:07
# Schema: mixs6
#
# id: http://w3id.org/mixs6
# description: MIxS 6 linkml rendering
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from includes.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
MIXS = CurieNamespace('MIXS', 'https://w3id.org/mixs/terms/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
MIXS_VOCAB = CurieNamespace('mixs_vocab', 'https://w3id.org/mixs/vocab/')
DEFAULT_ = MIXS.VOCAB


# Types

# Class references



@dataclass
class Core(YAMLRoot):
    """
    core package
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB.Core
    class_class_curie: ClassVar[str] = "mixs.vocab:Core"
    class_name: ClassVar[str] = "core"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Core

    submitted_to_insdc: Optional[str] = None
    investigation_type: Optional[str] = None
    sample_name: Optional[str] = None
    project_name: Optional[str] = None
    experimental_factor: Optional[str] = None
    lat_lon: Optional[str] = None
    depth: Optional[str] = None
    alt: Optional[str] = None
    elev: Optional[str] = None
    geo_loc_name: Optional[str] = None
    collection_date: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    env_package: Optional[str] = None
    subspecf_gen_lin: Optional[str] = None
    ploidy: Optional[str] = None
    num_replicons: Optional[str] = None
    extrachrom_elements: Optional[str] = None
    estimated_size: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    source_mat_id: Optional[str] = None
    pathogenicity: Optional[str] = None
    biotic_relationship: Optional[str] = None
    specific_host: Optional[str] = None
    host_spec_range: Optional[str] = None
    health_disease_stat: Optional[str] = None
    trophic_level: Optional[str] = None
    propagation: Optional[str] = None
    encoded_traits: Optional[str] = None
    rel_to_oxygen: Optional[str] = None
    isol_growth_condt: Optional[str] = None
    samp_collect_device: Optional[str] = None
    samp_mat_process: Optional[str] = None
    size_frac: Optional[str] = None
    samp_size: Optional[str] = None
    source_uvig: Optional[str] = None
    virus_enrich_appr: Optional[str] = None
    nucl_acid_ext: Optional[str] = None
    nucl_acid_amp: Optional[str] = None
    lib_size: Optional[str] = None
    lib_reads_seqd: Optional[str] = None
    lib_layout: Optional[str] = None
    lib_vector: Optional[str] = None
    lib_screen: Optional[str] = None
    target_gene: Optional[str] = None
    target_subfragment: Optional[str] = None
    pcr_primers: Optional[str] = None
    mid: Optional[str] = None
    adapters: Optional[str] = None
    pcr_cond: Optional[str] = None
    seq_meth: Optional[str] = None
    seq_quality_check: Optional[str] = None
    chimera_check: Optional[str] = None
    tax_ident: Optional[str] = None
    assembly_qual: Optional[str] = None
    assembly_name: Optional[str] = None
    assembly_software: Optional[str] = None
    annot: Optional[str] = None
    number_contig: Optional[str] = None
    feat_pred: Optional[str] = None
    ref_db: Optional[str] = None
    sim_search_meth: Optional[str] = None
    tax_class: Optional[str] = None
    x_16s_recover: Optional[str] = None
    x_16s_recover_software: Optional[str] = None
    trnas: Optional[str] = None
    trna_ext_software: Optional[str] = None
    compl_score: Optional[str] = None
    compl_software: Optional[str] = None
    compl_appr: Optional[str] = None
    contam_score: Optional[str] = None
    contam_screen_input: Optional[str] = None
    contam_screen_param: Optional[str] = None
    decontam_software: Optional[str] = None
    sort_tech: Optional[str] = None
    single_cell_lysis_appr: Optional[str] = None
    single_cell_lysis_prot: Optional[str] = None
    wga_amp_appr: Optional[str] = None
    wga_amp_kit: Optional[str] = None
    bin_param: Optional[str] = None
    bin_software: Optional[str] = None
    reassembly_bin: Optional[str] = None
    mag_cov_software: Optional[str] = None
    vir_ident_software: Optional[str] = None
    pred_genome_type: Optional[str] = None
    pred_genome_struc: Optional[str] = None
    detec_type: Optional[str] = None
    votu_class_appr: Optional[str] = None
    votu_seq_comp_appr: Optional[str] = None
    votu_db: Optional[str] = None
    host_pred_appr: Optional[str] = None
    host_pred_est_acc: Optional[str] = None
    url: Optional[str] = None
    sop: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.submitted_to_insdc is not None and not isinstance(self.submitted_to_insdc, str):
            self.submitted_to_insdc = str(self.submitted_to_insdc)

        if self.investigation_type is not None and not isinstance(self.investigation_type, str):
            self.investigation_type = str(self.investigation_type)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.project_name is not None and not isinstance(self.project_name, str):
            self.project_name = str(self.project_name)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.lat_lon is not None and not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.elev is not None and not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self.collection_date is not None and not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.env_package is not None and not isinstance(self.env_package, str):
            self.env_package = str(self.env_package)

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.ploidy is not None and not isinstance(self.ploidy, str):
            self.ploidy = str(self.ploidy)

        if self.num_replicons is not None and not isinstance(self.num_replicons, str):
            self.num_replicons = str(self.num_replicons)

        if self.extrachrom_elements is not None and not isinstance(self.extrachrom_elements, str):
            self.extrachrom_elements = str(self.extrachrom_elements)

        if self.estimated_size is not None and not isinstance(self.estimated_size, str):
            self.estimated_size = str(self.estimated_size)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, str):
            self.biotic_relationship = str(self.biotic_relationship)

        if self.specific_host is not None and not isinstance(self.specific_host, str):
            self.specific_host = str(self.specific_host)

        if self.host_spec_range is not None and not isinstance(self.host_spec_range, str):
            self.host_spec_range = str(self.host_spec_range)

        if self.health_disease_stat is not None and not isinstance(self.health_disease_stat, str):
            self.health_disease_stat = str(self.health_disease_stat)

        if self.trophic_level is not None and not isinstance(self.trophic_level, str):
            self.trophic_level = str(self.trophic_level)

        if self.propagation is not None and not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, str):
            self.rel_to_oxygen = str(self.rel_to_oxygen)

        if self.isol_growth_condt is not None and not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self.samp_collect_device is not None and not isinstance(self.samp_collect_device, str):
            self.samp_collect_device = str(self.samp_collect_device)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.size_frac is not None and not isinstance(self.size_frac, str):
            self.size_frac = str(self.size_frac)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.source_uvig is not None and not isinstance(self.source_uvig, str):
            self.source_uvig = str(self.source_uvig)

        if self.virus_enrich_appr is not None and not isinstance(self.virus_enrich_appr, str):
            self.virus_enrich_appr = str(self.virus_enrich_appr)

        if self.nucl_acid_ext is not None and not isinstance(self.nucl_acid_ext, str):
            self.nucl_acid_ext = str(self.nucl_acid_ext)

        if self.nucl_acid_amp is not None and not isinstance(self.nucl_acid_amp, str):
            self.nucl_acid_amp = str(self.nucl_acid_amp)

        if self.lib_size is not None and not isinstance(self.lib_size, str):
            self.lib_size = str(self.lib_size)

        if self.lib_reads_seqd is not None and not isinstance(self.lib_reads_seqd, str):
            self.lib_reads_seqd = str(self.lib_reads_seqd)

        if self.lib_layout is not None and not isinstance(self.lib_layout, str):
            self.lib_layout = str(self.lib_layout)

        if self.lib_vector is not None and not isinstance(self.lib_vector, str):
            self.lib_vector = str(self.lib_vector)

        if self.lib_screen is not None and not isinstance(self.lib_screen, str):
            self.lib_screen = str(self.lib_screen)

        if self.target_gene is not None and not isinstance(self.target_gene, str):
            self.target_gene = str(self.target_gene)

        if self.target_subfragment is not None and not isinstance(self.target_subfragment, str):
            self.target_subfragment = str(self.target_subfragment)

        if self.pcr_primers is not None and not isinstance(self.pcr_primers, str):
            self.pcr_primers = str(self.pcr_primers)

        if self.mid is not None and not isinstance(self.mid, str):
            self.mid = str(self.mid)

        if self.adapters is not None and not isinstance(self.adapters, str):
            self.adapters = str(self.adapters)

        if self.pcr_cond is not None and not isinstance(self.pcr_cond, str):
            self.pcr_cond = str(self.pcr_cond)

        if self.seq_meth is not None and not isinstance(self.seq_meth, str):
            self.seq_meth = str(self.seq_meth)

        if self.seq_quality_check is not None and not isinstance(self.seq_quality_check, str):
            self.seq_quality_check = str(self.seq_quality_check)

        if self.chimera_check is not None and not isinstance(self.chimera_check, str):
            self.chimera_check = str(self.chimera_check)

        if self.tax_ident is not None and not isinstance(self.tax_ident, str):
            self.tax_ident = str(self.tax_ident)

        if self.assembly_qual is not None and not isinstance(self.assembly_qual, str):
            self.assembly_qual = str(self.assembly_qual)

        if self.assembly_name is not None and not isinstance(self.assembly_name, str):
            self.assembly_name = str(self.assembly_name)

        if self.assembly_software is not None and not isinstance(self.assembly_software, str):
            self.assembly_software = str(self.assembly_software)

        if self.annot is not None and not isinstance(self.annot, str):
            self.annot = str(self.annot)

        if self.number_contig is not None and not isinstance(self.number_contig, str):
            self.number_contig = str(self.number_contig)

        if self.feat_pred is not None and not isinstance(self.feat_pred, str):
            self.feat_pred = str(self.feat_pred)

        if self.ref_db is not None and not isinstance(self.ref_db, str):
            self.ref_db = str(self.ref_db)

        if self.sim_search_meth is not None and not isinstance(self.sim_search_meth, str):
            self.sim_search_meth = str(self.sim_search_meth)

        if self.tax_class is not None and not isinstance(self.tax_class, str):
            self.tax_class = str(self.tax_class)

        if self.x_16s_recover is not None and not isinstance(self.x_16s_recover, str):
            self.x_16s_recover = str(self.x_16s_recover)

        if self.x_16s_recover_software is not None and not isinstance(self.x_16s_recover_software, str):
            self.x_16s_recover_software = str(self.x_16s_recover_software)

        if self.trnas is not None and not isinstance(self.trnas, str):
            self.trnas = str(self.trnas)

        if self.trna_ext_software is not None and not isinstance(self.trna_ext_software, str):
            self.trna_ext_software = str(self.trna_ext_software)

        if self.compl_score is not None and not isinstance(self.compl_score, str):
            self.compl_score = str(self.compl_score)

        if self.compl_software is not None and not isinstance(self.compl_software, str):
            self.compl_software = str(self.compl_software)

        if self.compl_appr is not None and not isinstance(self.compl_appr, str):
            self.compl_appr = str(self.compl_appr)

        if self.contam_score is not None and not isinstance(self.contam_score, str):
            self.contam_score = str(self.contam_score)

        if self.contam_screen_input is not None and not isinstance(self.contam_screen_input, str):
            self.contam_screen_input = str(self.contam_screen_input)

        if self.contam_screen_param is not None and not isinstance(self.contam_screen_param, str):
            self.contam_screen_param = str(self.contam_screen_param)

        if self.decontam_software is not None and not isinstance(self.decontam_software, str):
            self.decontam_software = str(self.decontam_software)

        if self.sort_tech is not None and not isinstance(self.sort_tech, str):
            self.sort_tech = str(self.sort_tech)

        if self.single_cell_lysis_appr is not None and not isinstance(self.single_cell_lysis_appr, str):
            self.single_cell_lysis_appr = str(self.single_cell_lysis_appr)

        if self.single_cell_lysis_prot is not None and not isinstance(self.single_cell_lysis_prot, str):
            self.single_cell_lysis_prot = str(self.single_cell_lysis_prot)

        if self.wga_amp_appr is not None and not isinstance(self.wga_amp_appr, str):
            self.wga_amp_appr = str(self.wga_amp_appr)

        if self.wga_amp_kit is not None and not isinstance(self.wga_amp_kit, str):
            self.wga_amp_kit = str(self.wga_amp_kit)

        if self.bin_param is not None and not isinstance(self.bin_param, str):
            self.bin_param = str(self.bin_param)

        if self.bin_software is not None and not isinstance(self.bin_software, str):
            self.bin_software = str(self.bin_software)

        if self.reassembly_bin is not None and not isinstance(self.reassembly_bin, str):
            self.reassembly_bin = str(self.reassembly_bin)

        if self.mag_cov_software is not None and not isinstance(self.mag_cov_software, str):
            self.mag_cov_software = str(self.mag_cov_software)

        if self.vir_ident_software is not None and not isinstance(self.vir_ident_software, str):
            self.vir_ident_software = str(self.vir_ident_software)

        if self.pred_genome_type is not None and not isinstance(self.pred_genome_type, str):
            self.pred_genome_type = str(self.pred_genome_type)

        if self.pred_genome_struc is not None and not isinstance(self.pred_genome_struc, str):
            self.pred_genome_struc = str(self.pred_genome_struc)

        if self.detec_type is not None and not isinstance(self.detec_type, str):
            self.detec_type = str(self.detec_type)

        if self.votu_class_appr is not None and not isinstance(self.votu_class_appr, str):
            self.votu_class_appr = str(self.votu_class_appr)

        if self.votu_seq_comp_appr is not None and not isinstance(self.votu_seq_comp_appr, str):
            self.votu_seq_comp_appr = str(self.votu_seq_comp_appr)

        if self.votu_db is not None and not isinstance(self.votu_db, str):
            self.votu_db = str(self.votu_db)

        if self.host_pred_appr is not None and not isinstance(self.host_pred_appr, str):
            self.host_pred_appr = str(self.host_pred_appr)

        if self.host_pred_est_acc is not None and not isinstance(self.host_pred_est_acc, str):
            self.host_pred_est_acc = str(self.host_pred_est_acc)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.sop is not None and not isinstance(self.sop, str):
            self.sop = str(self.sop)

        super().__post_init__(**kwargs)


@dataclass
class Air(YAMLRoot):
    """
    air
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB.Air
    class_class_curie: ClassVar[str] = "mixs.vocab:Air"
    class_name: ClassVar[str] = "air"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Air

    barometric_press: Optional[str] = None
    carb_dioxide: Optional[str] = None
    carb_monoxide: Optional[str] = None
    chem_administration: Optional[str] = None
    humidity: Optional[str] = None
    methane: Optional[str] = None
    misc_param: Optional[str] = None
    organism_count: Optional[str] = None
    oxygen: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    perturbation: Optional[str] = None
    pollutants: Optional[str] = None
    resp_part_matter: Optional[str] = None
    samp_salinity: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    solar_irradiance: Optional[str] = None
    temp: Optional[str] = None
    ventilation_rate: Optional[str] = None
    ventilation_type: Optional[str] = None
    volatile_org_comp: Optional[str] = None
    wind_direction: Optional[str] = None
    wind_speed: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.barometric_press is not None and not isinstance(self.barometric_press, str):
            self.barometric_press = str(self.barometric_press)

        if self.carb_dioxide is not None and not isinstance(self.carb_dioxide, str):
            self.carb_dioxide = str(self.carb_dioxide)

        if self.carb_monoxide is not None and not isinstance(self.carb_monoxide, str):
            self.carb_monoxide = str(self.carb_monoxide)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.humidity is not None and not isinstance(self.humidity, str):
            self.humidity = str(self.humidity)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.oxygen is not None and not isinstance(self.oxygen, str):
            self.oxygen = str(self.oxygen)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.pollutants is not None and not isinstance(self.pollutants, str):
            self.pollutants = str(self.pollutants)

        if self.resp_part_matter is not None and not isinstance(self.resp_part_matter, str):
            self.resp_part_matter = str(self.resp_part_matter)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.solar_irradiance is not None and not isinstance(self.solar_irradiance, str):
            self.solar_irradiance = str(self.solar_irradiance)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.ventilation_rate is not None and not isinstance(self.ventilation_rate, str):
            self.ventilation_rate = str(self.ventilation_rate)

        if self.ventilation_type is not None and not isinstance(self.ventilation_type, str):
            self.ventilation_type = str(self.ventilation_type)

        if self.volatile_org_comp is not None and not isinstance(self.volatile_org_comp, str):
            self.volatile_org_comp = str(self.volatile_org_comp)

        if self.wind_direction is not None and not isinstance(self.wind_direction, str):
            self.wind_direction = str(self.wind_direction)

        if self.wind_speed is not None and not isinstance(self.wind_speed, str):
            self.wind_speed = str(self.wind_speed)

        super().__post_init__(**kwargs)


@dataclass
class BuiltEnvironment(YAMLRoot):
    """
    built environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB.BuiltEnvironment
    class_class_curie: ClassVar[str] = "mixs.vocab:BuiltEnvironment"
    class_name: ClassVar[str] = "built environment"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.BuiltEnvironment

    surf_material: Optional[str] = None
    surf_air_cont: Optional[str] = None
    rel_air_humidity: Optional[str] = None
    abs_air_humidity: Optional[str] = None
    surf_humidity: Optional[str] = None
    air_temp: Optional[str] = None
    surf_temp: Optional[str] = None
    surf_moisture_ph: Optional[str] = None
    build_occup_type: Optional[str] = None
    surf_moisture: Optional[str] = None
    dew_point: Optional[str] = None
    carb_dioxide: Optional[str] = None
    ventilation_type: Optional[str] = None
    organism_count: Optional[str] = None
    indoor_space: Optional[str] = None
    indoor_surf: Optional[str] = None
    filter_type: Optional[str] = None
    heat_cool_type: Optional[str] = None
    substructure_type: Optional[str] = None
    building_setting: Optional[str] = None
    light_type: Optional[str] = None
    samp_sort_meth: Optional[str] = None
    space_typ_state: Optional[str] = None
    typ_occup_density: Optional[str] = None
    occup_samp: Optional[str] = None
    occup_density_samp: Optional[str] = None
    address: Optional[str] = None
    adj_room: Optional[str] = None
    aero_struc: Optional[str] = None
    amount_light: Optional[str] = None
    arch_struc: Optional[str] = None
    avg_occup: Optional[str] = None
    avg_dew_point: Optional[str] = None
    avg_temp: Optional[str] = None
    bathroom_count: Optional[str] = None
    bedroom_count: Optional[str] = None
    built_struc_age: Optional[str] = None
    built_struc_set: Optional[str] = None
    built_struc_type: Optional[str] = None
    ceil_area: Optional[str] = None
    ceil_cond: Optional[str] = None
    ceil_finish_mat: Optional[str] = None
    ceil_water_mold: Optional[str] = None
    ceil_struc: Optional[str] = None
    ceil_texture: Optional[str] = None
    ceil_thermal_mass: Optional[str] = None
    ceil_type: Optional[str] = None
    cool_syst_id: Optional[str] = None
    date_last_rain: Optional[str] = None
    build_docs: Optional[str] = None
    door_size: Optional[str] = None
    door_cond: Optional[str] = None
    door_direct: Optional[str] = None
    door_loc: Optional[str] = None
    door_mat: Optional[str] = None
    door_move: Optional[str] = None
    door_water_mold: Optional[str] = None
    door_type: Optional[str] = None
    door_comp_type: Optional[str] = None
    door_type_metal: Optional[str] = None
    door_type_wood: Optional[str] = None
    drawings: Optional[str] = None
    elevator: Optional[str] = None
    escalator: Optional[str] = None
    exp_duct: Optional[str] = None
    exp_pipe: Optional[str] = None
    ext_door: Optional[str] = None
    fireplace_type: Optional[str] = None
    floor_age: Optional[str] = None
    floor_area: Optional[str] = None
    floor_cond: Optional[str] = None
    floor_count: Optional[str] = None
    floor_finish_mat: Optional[str] = None
    floor_water_mold: Optional[str] = None
    floor_struc: Optional[str] = None
    floor_thermal_mass: Optional[str] = None
    freq_clean: Optional[str] = None
    freq_cook: Optional[str] = None
    furniture: Optional[str] = None
    gender_restroom: Optional[str] = None
    hall_count: Optional[str] = None
    handidness: Optional[str] = None
    heat_deliv_loc: Optional[str] = None
    heat_system_deliv_meth: Optional[str] = None
    heat_system_id: Optional[str] = None
    height_carper_fiber: Optional[str] = None
    inside_lux: Optional[str] = None
    int_wall_cond: Optional[str] = None
    last_clean: Optional[str] = None
    max_occup: Optional[str] = None
    mech_struc: Optional[str] = None
    number_plants: Optional[str] = None
    number_pets: Optional[str] = None
    number_resident: Optional[str] = None
    occup_document: Optional[str] = None
    ext_wall_orient: Optional[str] = None
    ext_window_orient: Optional[str] = None
    rel_humidity_out: Optional[str] = None
    pres_animal: Optional[str] = None
    quad_pos: Optional[str] = None
    rel_samp_loc: Optional[str] = None
    room_air_exch_rate: Optional[str] = None
    room_architec_element: Optional[str] = None
    room_condt: Optional[str] = None
    room_count: Optional[str] = None
    room_dim: Optional[str] = None
    room_door_dist: Optional[str] = None
    room_loc: Optional[str] = None
    room_moist_damage_hist: Optional[str] = None
    room_net_area: Optional[str] = None
    room_occup: Optional[str] = None
    room_samp_pos: Optional[str] = None
    room_type: Optional[str] = None
    room_vol: Optional[str] = None
    room_window_count: Optional[str] = None
    room_connected: Optional[str] = None
    room_hallway: Optional[str] = None
    room_door_share: Optional[str] = None
    room_wall_share: Optional[str] = None
    samp_weather: Optional[str] = None
    samp_floor: Optional[str] = None
    samp_room_id: Optional[str] = None
    samp_time_out: Optional[str] = None
    season: Optional[str] = None
    season_use: Optional[str] = None
    shading_device_cond: Optional[str] = None
    shading_device_loc: Optional[str] = None
    shading_device_mat: Optional[str] = None
    shading_device_water_mold: Optional[str] = None
    shading_device_type: Optional[str] = None
    specific_humidity: Optional[str] = None
    specific: Optional[str] = None
    temp_out: Optional[str] = None
    train_line: Optional[str] = None
    train_stat_loc: Optional[str] = None
    train_stop_loc: Optional[str] = None
    vis_media: Optional[str] = None
    wall_area: Optional[str] = None
    wall_const_type: Optional[str] = None
    wall_finish_mat: Optional[str] = None
    wall_height: Optional[str] = None
    wall_loc: Optional[str] = None
    wall_water_mold: Optional[str] = None
    wall_surf_treatment: Optional[str] = None
    wall_texture: Optional[str] = None
    wall_thermal_mass: Optional[str] = None
    water_feat_size: Optional[str] = None
    water_feat_type: Optional[str] = None
    weekday: Optional[str] = None
    window_size: Optional[str] = None
    window_cond: Optional[str] = None
    window_cover: Optional[str] = None
    window_horiz_pos: Optional[str] = None
    window_loc: Optional[str] = None
    window_mat: Optional[str] = None
    window_open_freq: Optional[str] = None
    window_water_mold: Optional[str] = None
    window_status: Optional[str] = None
    window_type: Optional[str] = None
    window_vert_pos: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.surf_material is not None and not isinstance(self.surf_material, str):
            self.surf_material = str(self.surf_material)

        if self.surf_air_cont is not None and not isinstance(self.surf_air_cont, str):
            self.surf_air_cont = str(self.surf_air_cont)

        if self.rel_air_humidity is not None and not isinstance(self.rel_air_humidity, str):
            self.rel_air_humidity = str(self.rel_air_humidity)

        if self.abs_air_humidity is not None and not isinstance(self.abs_air_humidity, str):
            self.abs_air_humidity = str(self.abs_air_humidity)

        if self.surf_humidity is not None and not isinstance(self.surf_humidity, str):
            self.surf_humidity = str(self.surf_humidity)

        if self.air_temp is not None and not isinstance(self.air_temp, str):
            self.air_temp = str(self.air_temp)

        if self.surf_temp is not None and not isinstance(self.surf_temp, str):
            self.surf_temp = str(self.surf_temp)

        if self.surf_moisture_ph is not None and not isinstance(self.surf_moisture_ph, str):
            self.surf_moisture_ph = str(self.surf_moisture_ph)

        if self.build_occup_type is not None and not isinstance(self.build_occup_type, str):
            self.build_occup_type = str(self.build_occup_type)

        if self.surf_moisture is not None and not isinstance(self.surf_moisture, str):
            self.surf_moisture = str(self.surf_moisture)

        if self.dew_point is not None and not isinstance(self.dew_point, str):
            self.dew_point = str(self.dew_point)

        if self.carb_dioxide is not None and not isinstance(self.carb_dioxide, str):
            self.carb_dioxide = str(self.carb_dioxide)

        if self.ventilation_type is not None and not isinstance(self.ventilation_type, str):
            self.ventilation_type = str(self.ventilation_type)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.indoor_space is not None and not isinstance(self.indoor_space, str):
            self.indoor_space = str(self.indoor_space)

        if self.indoor_surf is not None and not isinstance(self.indoor_surf, str):
            self.indoor_surf = str(self.indoor_surf)

        if self.filter_type is not None and not isinstance(self.filter_type, str):
            self.filter_type = str(self.filter_type)

        if self.heat_cool_type is not None and not isinstance(self.heat_cool_type, str):
            self.heat_cool_type = str(self.heat_cool_type)

        if self.substructure_type is not None and not isinstance(self.substructure_type, str):
            self.substructure_type = str(self.substructure_type)

        if self.building_setting is not None and not isinstance(self.building_setting, str):
            self.building_setting = str(self.building_setting)

        if self.light_type is not None and not isinstance(self.light_type, str):
            self.light_type = str(self.light_type)

        if self.samp_sort_meth is not None and not isinstance(self.samp_sort_meth, str):
            self.samp_sort_meth = str(self.samp_sort_meth)

        if self.space_typ_state is not None and not isinstance(self.space_typ_state, str):
            self.space_typ_state = str(self.space_typ_state)

        if self.typ_occup_density is not None and not isinstance(self.typ_occup_density, str):
            self.typ_occup_density = str(self.typ_occup_density)

        if self.occup_samp is not None and not isinstance(self.occup_samp, str):
            self.occup_samp = str(self.occup_samp)

        if self.occup_density_samp is not None and not isinstance(self.occup_density_samp, str):
            self.occup_density_samp = str(self.occup_density_samp)

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.adj_room is not None and not isinstance(self.adj_room, str):
            self.adj_room = str(self.adj_room)

        if self.aero_struc is not None and not isinstance(self.aero_struc, str):
            self.aero_struc = str(self.aero_struc)

        if self.amount_light is not None and not isinstance(self.amount_light, str):
            self.amount_light = str(self.amount_light)

        if self.arch_struc is not None and not isinstance(self.arch_struc, str):
            self.arch_struc = str(self.arch_struc)

        if self.avg_occup is not None and not isinstance(self.avg_occup, str):
            self.avg_occup = str(self.avg_occup)

        if self.avg_dew_point is not None and not isinstance(self.avg_dew_point, str):
            self.avg_dew_point = str(self.avg_dew_point)

        if self.avg_temp is not None and not isinstance(self.avg_temp, str):
            self.avg_temp = str(self.avg_temp)

        if self.bathroom_count is not None and not isinstance(self.bathroom_count, str):
            self.bathroom_count = str(self.bathroom_count)

        if self.bedroom_count is not None and not isinstance(self.bedroom_count, str):
            self.bedroom_count = str(self.bedroom_count)

        if self.built_struc_age is not None and not isinstance(self.built_struc_age, str):
            self.built_struc_age = str(self.built_struc_age)

        if self.built_struc_set is not None and not isinstance(self.built_struc_set, str):
            self.built_struc_set = str(self.built_struc_set)

        if self.built_struc_type is not None and not isinstance(self.built_struc_type, str):
            self.built_struc_type = str(self.built_struc_type)

        if self.ceil_area is not None and not isinstance(self.ceil_area, str):
            self.ceil_area = str(self.ceil_area)

        if self.ceil_cond is not None and not isinstance(self.ceil_cond, str):
            self.ceil_cond = str(self.ceil_cond)

        if self.ceil_finish_mat is not None and not isinstance(self.ceil_finish_mat, str):
            self.ceil_finish_mat = str(self.ceil_finish_mat)

        if self.ceil_water_mold is not None and not isinstance(self.ceil_water_mold, str):
            self.ceil_water_mold = str(self.ceil_water_mold)

        if self.ceil_struc is not None and not isinstance(self.ceil_struc, str):
            self.ceil_struc = str(self.ceil_struc)

        if self.ceil_texture is not None and not isinstance(self.ceil_texture, str):
            self.ceil_texture = str(self.ceil_texture)

        if self.ceil_thermal_mass is not None and not isinstance(self.ceil_thermal_mass, str):
            self.ceil_thermal_mass = str(self.ceil_thermal_mass)

        if self.ceil_type is not None and not isinstance(self.ceil_type, str):
            self.ceil_type = str(self.ceil_type)

        if self.cool_syst_id is not None and not isinstance(self.cool_syst_id, str):
            self.cool_syst_id = str(self.cool_syst_id)

        if self.date_last_rain is not None and not isinstance(self.date_last_rain, str):
            self.date_last_rain = str(self.date_last_rain)

        if self.build_docs is not None and not isinstance(self.build_docs, str):
            self.build_docs = str(self.build_docs)

        if self.door_size is not None and not isinstance(self.door_size, str):
            self.door_size = str(self.door_size)

        if self.door_cond is not None and not isinstance(self.door_cond, str):
            self.door_cond = str(self.door_cond)

        if self.door_direct is not None and not isinstance(self.door_direct, str):
            self.door_direct = str(self.door_direct)

        if self.door_loc is not None and not isinstance(self.door_loc, str):
            self.door_loc = str(self.door_loc)

        if self.door_mat is not None and not isinstance(self.door_mat, str):
            self.door_mat = str(self.door_mat)

        if self.door_move is not None and not isinstance(self.door_move, str):
            self.door_move = str(self.door_move)

        if self.door_water_mold is not None and not isinstance(self.door_water_mold, str):
            self.door_water_mold = str(self.door_water_mold)

        if self.door_type is not None and not isinstance(self.door_type, str):
            self.door_type = str(self.door_type)

        if self.door_comp_type is not None and not isinstance(self.door_comp_type, str):
            self.door_comp_type = str(self.door_comp_type)

        if self.door_type_metal is not None and not isinstance(self.door_type_metal, str):
            self.door_type_metal = str(self.door_type_metal)

        if self.door_type_wood is not None and not isinstance(self.door_type_wood, str):
            self.door_type_wood = str(self.door_type_wood)

        if self.drawings is not None and not isinstance(self.drawings, str):
            self.drawings = str(self.drawings)

        if self.elevator is not None and not isinstance(self.elevator, str):
            self.elevator = str(self.elevator)

        if self.escalator is not None and not isinstance(self.escalator, str):
            self.escalator = str(self.escalator)

        if self.exp_duct is not None and not isinstance(self.exp_duct, str):
            self.exp_duct = str(self.exp_duct)

        if self.exp_pipe is not None and not isinstance(self.exp_pipe, str):
            self.exp_pipe = str(self.exp_pipe)

        if self.ext_door is not None and not isinstance(self.ext_door, str):
            self.ext_door = str(self.ext_door)

        if self.fireplace_type is not None and not isinstance(self.fireplace_type, str):
            self.fireplace_type = str(self.fireplace_type)

        if self.floor_age is not None and not isinstance(self.floor_age, str):
            self.floor_age = str(self.floor_age)

        if self.floor_area is not None and not isinstance(self.floor_area, str):
            self.floor_area = str(self.floor_area)

        if self.floor_cond is not None and not isinstance(self.floor_cond, str):
            self.floor_cond = str(self.floor_cond)

        if self.floor_count is not None and not isinstance(self.floor_count, str):
            self.floor_count = str(self.floor_count)

        if self.floor_finish_mat is not None and not isinstance(self.floor_finish_mat, str):
            self.floor_finish_mat = str(self.floor_finish_mat)

        if self.floor_water_mold is not None and not isinstance(self.floor_water_mold, str):
            self.floor_water_mold = str(self.floor_water_mold)

        if self.floor_struc is not None and not isinstance(self.floor_struc, str):
            self.floor_struc = str(self.floor_struc)

        if self.floor_thermal_mass is not None and not isinstance(self.floor_thermal_mass, str):
            self.floor_thermal_mass = str(self.floor_thermal_mass)

        if self.freq_clean is not None and not isinstance(self.freq_clean, str):
            self.freq_clean = str(self.freq_clean)

        if self.freq_cook is not None and not isinstance(self.freq_cook, str):
            self.freq_cook = str(self.freq_cook)

        if self.furniture is not None and not isinstance(self.furniture, str):
            self.furniture = str(self.furniture)

        if self.gender_restroom is not None and not isinstance(self.gender_restroom, str):
            self.gender_restroom = str(self.gender_restroom)

        if self.hall_count is not None and not isinstance(self.hall_count, str):
            self.hall_count = str(self.hall_count)

        if self.handidness is not None and not isinstance(self.handidness, str):
            self.handidness = str(self.handidness)

        if self.heat_deliv_loc is not None and not isinstance(self.heat_deliv_loc, str):
            self.heat_deliv_loc = str(self.heat_deliv_loc)

        if self.heat_system_deliv_meth is not None and not isinstance(self.heat_system_deliv_meth, str):
            self.heat_system_deliv_meth = str(self.heat_system_deliv_meth)

        if self.heat_system_id is not None and not isinstance(self.heat_system_id, str):
            self.heat_system_id = str(self.heat_system_id)

        if self.height_carper_fiber is not None and not isinstance(self.height_carper_fiber, str):
            self.height_carper_fiber = str(self.height_carper_fiber)

        if self.inside_lux is not None and not isinstance(self.inside_lux, str):
            self.inside_lux = str(self.inside_lux)

        if self.int_wall_cond is not None and not isinstance(self.int_wall_cond, str):
            self.int_wall_cond = str(self.int_wall_cond)

        if self.last_clean is not None and not isinstance(self.last_clean, str):
            self.last_clean = str(self.last_clean)

        if self.max_occup is not None and not isinstance(self.max_occup, str):
            self.max_occup = str(self.max_occup)

        if self.mech_struc is not None and not isinstance(self.mech_struc, str):
            self.mech_struc = str(self.mech_struc)

        if self.number_plants is not None and not isinstance(self.number_plants, str):
            self.number_plants = str(self.number_plants)

        if self.number_pets is not None and not isinstance(self.number_pets, str):
            self.number_pets = str(self.number_pets)

        if self.number_resident is not None and not isinstance(self.number_resident, str):
            self.number_resident = str(self.number_resident)

        if self.occup_document is not None and not isinstance(self.occup_document, str):
            self.occup_document = str(self.occup_document)

        if self.ext_wall_orient is not None and not isinstance(self.ext_wall_orient, str):
            self.ext_wall_orient = str(self.ext_wall_orient)

        if self.ext_window_orient is not None and not isinstance(self.ext_window_orient, str):
            self.ext_window_orient = str(self.ext_window_orient)

        if self.rel_humidity_out is not None and not isinstance(self.rel_humidity_out, str):
            self.rel_humidity_out = str(self.rel_humidity_out)

        if self.pres_animal is not None and not isinstance(self.pres_animal, str):
            self.pres_animal = str(self.pres_animal)

        if self.quad_pos is not None and not isinstance(self.quad_pos, str):
            self.quad_pos = str(self.quad_pos)

        if self.rel_samp_loc is not None and not isinstance(self.rel_samp_loc, str):
            self.rel_samp_loc = str(self.rel_samp_loc)

        if self.room_air_exch_rate is not None and not isinstance(self.room_air_exch_rate, str):
            self.room_air_exch_rate = str(self.room_air_exch_rate)

        if self.room_architec_element is not None and not isinstance(self.room_architec_element, str):
            self.room_architec_element = str(self.room_architec_element)

        if self.room_condt is not None and not isinstance(self.room_condt, str):
            self.room_condt = str(self.room_condt)

        if self.room_count is not None and not isinstance(self.room_count, str):
            self.room_count = str(self.room_count)

        if self.room_dim is not None and not isinstance(self.room_dim, str):
            self.room_dim = str(self.room_dim)

        if self.room_door_dist is not None and not isinstance(self.room_door_dist, str):
            self.room_door_dist = str(self.room_door_dist)

        if self.room_loc is not None and not isinstance(self.room_loc, str):
            self.room_loc = str(self.room_loc)

        if self.room_moist_damage_hist is not None and not isinstance(self.room_moist_damage_hist, str):
            self.room_moist_damage_hist = str(self.room_moist_damage_hist)

        if self.room_net_area is not None and not isinstance(self.room_net_area, str):
            self.room_net_area = str(self.room_net_area)

        if self.room_occup is not None and not isinstance(self.room_occup, str):
            self.room_occup = str(self.room_occup)

        if self.room_samp_pos is not None and not isinstance(self.room_samp_pos, str):
            self.room_samp_pos = str(self.room_samp_pos)

        if self.room_type is not None and not isinstance(self.room_type, str):
            self.room_type = str(self.room_type)

        if self.room_vol is not None and not isinstance(self.room_vol, str):
            self.room_vol = str(self.room_vol)

        if self.room_window_count is not None and not isinstance(self.room_window_count, str):
            self.room_window_count = str(self.room_window_count)

        if self.room_connected is not None and not isinstance(self.room_connected, str):
            self.room_connected = str(self.room_connected)

        if self.room_hallway is not None and not isinstance(self.room_hallway, str):
            self.room_hallway = str(self.room_hallway)

        if self.room_door_share is not None and not isinstance(self.room_door_share, str):
            self.room_door_share = str(self.room_door_share)

        if self.room_wall_share is not None and not isinstance(self.room_wall_share, str):
            self.room_wall_share = str(self.room_wall_share)

        if self.samp_weather is not None and not isinstance(self.samp_weather, str):
            self.samp_weather = str(self.samp_weather)

        if self.samp_floor is not None and not isinstance(self.samp_floor, str):
            self.samp_floor = str(self.samp_floor)

        if self.samp_room_id is not None and not isinstance(self.samp_room_id, str):
            self.samp_room_id = str(self.samp_room_id)

        if self.samp_time_out is not None and not isinstance(self.samp_time_out, str):
            self.samp_time_out = str(self.samp_time_out)

        if self.season is not None and not isinstance(self.season, str):
            self.season = str(self.season)

        if self.season_use is not None and not isinstance(self.season_use, str):
            self.season_use = str(self.season_use)

        if self.shading_device_cond is not None and not isinstance(self.shading_device_cond, str):
            self.shading_device_cond = str(self.shading_device_cond)

        if self.shading_device_loc is not None and not isinstance(self.shading_device_loc, str):
            self.shading_device_loc = str(self.shading_device_loc)

        if self.shading_device_mat is not None and not isinstance(self.shading_device_mat, str):
            self.shading_device_mat = str(self.shading_device_mat)

        if self.shading_device_water_mold is not None and not isinstance(self.shading_device_water_mold, str):
            self.shading_device_water_mold = str(self.shading_device_water_mold)

        if self.shading_device_type is not None and not isinstance(self.shading_device_type, str):
            self.shading_device_type = str(self.shading_device_type)

        if self.specific_humidity is not None and not isinstance(self.specific_humidity, str):
            self.specific_humidity = str(self.specific_humidity)

        if self.specific is not None and not isinstance(self.specific, str):
            self.specific = str(self.specific)

        if self.temp_out is not None and not isinstance(self.temp_out, str):
            self.temp_out = str(self.temp_out)

        if self.train_line is not None and not isinstance(self.train_line, str):
            self.train_line = str(self.train_line)

        if self.train_stat_loc is not None and not isinstance(self.train_stat_loc, str):
            self.train_stat_loc = str(self.train_stat_loc)

        if self.train_stop_loc is not None and not isinstance(self.train_stop_loc, str):
            self.train_stop_loc = str(self.train_stop_loc)

        if self.vis_media is not None and not isinstance(self.vis_media, str):
            self.vis_media = str(self.vis_media)

        if self.wall_area is not None and not isinstance(self.wall_area, str):
            self.wall_area = str(self.wall_area)

        if self.wall_const_type is not None and not isinstance(self.wall_const_type, str):
            self.wall_const_type = str(self.wall_const_type)

        if self.wall_finish_mat is not None and not isinstance(self.wall_finish_mat, str):
            self.wall_finish_mat = str(self.wall_finish_mat)

        if self.wall_height is not None and not isinstance(self.wall_height, str):
            self.wall_height = str(self.wall_height)

        if self.wall_loc is not None and not isinstance(self.wall_loc, str):
            self.wall_loc = str(self.wall_loc)

        if self.wall_water_mold is not None and not isinstance(self.wall_water_mold, str):
            self.wall_water_mold = str(self.wall_water_mold)

        if self.wall_surf_treatment is not None and not isinstance(self.wall_surf_treatment, str):
            self.wall_surf_treatment = str(self.wall_surf_treatment)

        if self.wall_texture is not None and not isinstance(self.wall_texture, str):
            self.wall_texture = str(self.wall_texture)

        if self.wall_thermal_mass is not None and not isinstance(self.wall_thermal_mass, str):
            self.wall_thermal_mass = str(self.wall_thermal_mass)

        if self.water_feat_size is not None and not isinstance(self.water_feat_size, str):
            self.water_feat_size = str(self.water_feat_size)

        if self.water_feat_type is not None and not isinstance(self.water_feat_type, str):
            self.water_feat_type = str(self.water_feat_type)

        if self.weekday is not None and not isinstance(self.weekday, str):
            self.weekday = str(self.weekday)

        if self.window_size is not None and not isinstance(self.window_size, str):
            self.window_size = str(self.window_size)

        if self.window_cond is not None and not isinstance(self.window_cond, str):
            self.window_cond = str(self.window_cond)

        if self.window_cover is not None and not isinstance(self.window_cover, str):
            self.window_cover = str(self.window_cover)

        if self.window_horiz_pos is not None and not isinstance(self.window_horiz_pos, str):
            self.window_horiz_pos = str(self.window_horiz_pos)

        if self.window_loc is not None and not isinstance(self.window_loc, str):
            self.window_loc = str(self.window_loc)

        if self.window_mat is not None and not isinstance(self.window_mat, str):
            self.window_mat = str(self.window_mat)

        if self.window_open_freq is not None and not isinstance(self.window_open_freq, str):
            self.window_open_freq = str(self.window_open_freq)

        if self.window_water_mold is not None and not isinstance(self.window_water_mold, str):
            self.window_water_mold = str(self.window_water_mold)

        if self.window_status is not None and not isinstance(self.window_status, str):
            self.window_status = str(self.window_status)

        if self.window_type is not None and not isinstance(self.window_type, str):
            self.window_type = str(self.window_type)

        if self.window_vert_pos is not None and not isinstance(self.window_vert_pos, str):
            self.window_vert_pos = str(self.window_vert_pos)

        super().__post_init__(**kwargs)


@dataclass
class Host-associated(YAMLRoot):
    """
    host-associated
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB["Host-associated"]
    class_class_curie: ClassVar[str] = "mixs.vocab:Host-associated"
    class_name: ClassVar[str] = "host-associated"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Host-associated

    ances_data: Optional[str] = None
    biol_stat: Optional[str] = None
    genetic_mod: Optional[str] = None
    host_common_name: Optional[str] = None
    samp_capt_status: Optional[str] = None
    samp_dis_stage: Optional[str] = None
    host_taxid: Optional[str] = None
    host_subject_id: Optional[str] = None
    host_age: Optional[str] = None
    host_life_stage: Optional[str] = None
    host_sex: Optional[str] = None
    host_disease_stat: Optional[str] = None
    chem_administration: Optional[str] = None
    host_body_habitat: Optional[str] = None
    host_body_site: Optional[str] = None
    host_body_product: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_height: Optional[str] = None
    host_length: Optional[str] = None
    host_diet: Optional[str] = None
    host_last_meal: Optional[str] = None
    host_growth_cond: Optional[str] = None
    host_substrate: Optional[str] = None
    host_family_relationship: Optional[str] = None
    host_infra_specific_name: Optional[str] = None
    host_infra_specific_rank: Optional[str] = None
    host_genotype: Optional[str] = None
    host_phenotype: Optional[str] = None
    host_body_temp: Optional[str] = None
    host_dry_mass: Optional[str] = None
    host_blood_press_diast: Optional[str] = None
    host_blood_press_syst: Optional[str] = None
    host_color: Optional[str] = None
    host_shape: Optional[str] = None
    gravidity: Optional[str] = None
    perturbation: Optional[str] = None
    samp_salinity: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    temp: Optional[str] = None
    organism_count: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    misc_param: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ances_data is not None and not isinstance(self.ances_data, str):
            self.ances_data = str(self.ances_data)

        if self.biol_stat is not None and not isinstance(self.biol_stat, str):
            self.biol_stat = str(self.biol_stat)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.host_common_name is not None and not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self.samp_capt_status is not None and not isinstance(self.samp_capt_status, str):
            self.samp_capt_status = str(self.samp_capt_status)

        if self.samp_dis_stage is not None and not isinstance(self.samp_dis_stage, str):
            self.samp_dis_stage = str(self.samp_dis_stage)

        if self.host_taxid is not None and not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self.host_subject_id is not None and not isinstance(self.host_subject_id, str):
            self.host_subject_id = str(self.host_subject_id)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, str):
            self.host_life_stage = str(self.host_life_stage)

        if self.host_sex is not None and not isinstance(self.host_sex, str):
            self.host_sex = str(self.host_sex)

        if self.host_disease_stat is not None and not isinstance(self.host_disease_stat, str):
            self.host_disease_stat = str(self.host_disease_stat)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.host_body_habitat is not None and not isinstance(self.host_body_habitat, str):
            self.host_body_habitat = str(self.host_body_habitat)

        if self.host_body_site is not None and not isinstance(self.host_body_site, str):
            self.host_body_site = str(self.host_body_site)

        if self.host_body_product is not None and not isinstance(self.host_body_product, str):
            self.host_body_product = str(self.host_body_product)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_length is not None and not isinstance(self.host_length, str):
            self.host_length = str(self.host_length)

        if self.host_diet is not None and not isinstance(self.host_diet, str):
            self.host_diet = str(self.host_diet)

        if self.host_last_meal is not None and not isinstance(self.host_last_meal, str):
            self.host_last_meal = str(self.host_last_meal)

        if self.host_growth_cond is not None and not isinstance(self.host_growth_cond, str):
            self.host_growth_cond = str(self.host_growth_cond)

        if self.host_substrate is not None and not isinstance(self.host_substrate, str):
            self.host_substrate = str(self.host_substrate)

        if self.host_family_relationship is not None and not isinstance(self.host_family_relationship, str):
            self.host_family_relationship = str(self.host_family_relationship)

        if self.host_infra_specific_name is not None and not isinstance(self.host_infra_specific_name, str):
            self.host_infra_specific_name = str(self.host_infra_specific_name)

        if self.host_infra_specific_rank is not None and not isinstance(self.host_infra_specific_rank, str):
            self.host_infra_specific_rank = str(self.host_infra_specific_rank)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if self.host_body_temp is not None and not isinstance(self.host_body_temp, str):
            self.host_body_temp = str(self.host_body_temp)

        if self.host_dry_mass is not None and not isinstance(self.host_dry_mass, str):
            self.host_dry_mass = str(self.host_dry_mass)

        if self.host_blood_press_diast is not None and not isinstance(self.host_blood_press_diast, str):
            self.host_blood_press_diast = str(self.host_blood_press_diast)

        if self.host_blood_press_syst is not None and not isinstance(self.host_blood_press_syst, str):
            self.host_blood_press_syst = str(self.host_blood_press_syst)

        if self.host_color is not None and not isinstance(self.host_color, str):
            self.host_color = str(self.host_color)

        if self.host_shape is not None and not isinstance(self.host_shape, str):
            self.host_shape = str(self.host_shape)

        if self.gravidity is not None and not isinstance(self.gravidity, str):
            self.gravidity = str(self.gravidity)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        super().__post_init__(**kwargs)


@dataclass
class Human-associated(YAMLRoot):
    """
    human-associated
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB["Human-associated"]
    class_class_curie: ClassVar[str] = "mixs.vocab:Human-associated"
    class_name: ClassVar[str] = "human-associated"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Human-associated

    host_subject_id: Optional[str] = None
    host_age: Optional[str] = None
    host_sex: Optional[str] = None
    host_disease_stat: Optional[str] = None
    ihmc_medication_code: Optional[str] = None
    chem_administration: Optional[str] = None
    host_body_site: Optional[str] = None
    host_body_product: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_height: Optional[str] = None
    host_diet: Optional[str] = None
    host_last_meal: Optional[str] = None
    host_family_relationship: Optional[str] = None
    host_genotype: Optional[str] = None
    host_phenotype: Optional[str] = None
    host_body_temp: Optional[str] = None
    smoker: Optional[str] = None
    host_hiv_stat: Optional[str] = None
    drug_usage: Optional[str] = None
    host_body_mass_index: Optional[str] = None
    diet_last_six_month: Optional[str] = None
    weight_loss_3_month: Optional[str] = None
    ihmc_ethnicity: Optional[str] = None
    host_occupation: Optional[str] = None
    pet_farm_animal: Optional[str] = None
    travel_out_six_month: Optional[str] = None
    twin_sibling: Optional[str] = None
    medic_hist_perform: Optional[str] = None
    study_complt_stat: Optional[str] = None
    pulmonary_disord: Optional[str] = None
    nose_throat_disord: Optional[str] = None
    blood_blood_disord: Optional[str] = None
    host_pulse: Optional[str] = None
    gestation_state: Optional[str] = None
    maternal_health_stat: Optional[str] = None
    foetal_health_stat: Optional[str] = None
    amniotic_fluid_color: Optional[str] = None
    urogenit_tract_disor: Optional[str] = None
    urine_collect_meth: Optional[str] = None
    perturbation: Optional[str] = None
    samp_salinity: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    temp: Optional[str] = None
    organism_count: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    misc_param: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.host_subject_id is not None and not isinstance(self.host_subject_id, str):
            self.host_subject_id = str(self.host_subject_id)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_sex is not None and not isinstance(self.host_sex, str):
            self.host_sex = str(self.host_sex)

        if self.host_disease_stat is not None and not isinstance(self.host_disease_stat, str):
            self.host_disease_stat = str(self.host_disease_stat)

        if self.ihmc_medication_code is not None and not isinstance(self.ihmc_medication_code, str):
            self.ihmc_medication_code = str(self.ihmc_medication_code)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.host_body_site is not None and not isinstance(self.host_body_site, str):
            self.host_body_site = str(self.host_body_site)

        if self.host_body_product is not None and not isinstance(self.host_body_product, str):
            self.host_body_product = str(self.host_body_product)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_diet is not None and not isinstance(self.host_diet, str):
            self.host_diet = str(self.host_diet)

        if self.host_last_meal is not None and not isinstance(self.host_last_meal, str):
            self.host_last_meal = str(self.host_last_meal)

        if self.host_family_relationship is not None and not isinstance(self.host_family_relationship, str):
            self.host_family_relationship = str(self.host_family_relationship)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if self.host_body_temp is not None and not isinstance(self.host_body_temp, str):
            self.host_body_temp = str(self.host_body_temp)

        if self.smoker is not None and not isinstance(self.smoker, str):
            self.smoker = str(self.smoker)

        if self.host_hiv_stat is not None and not isinstance(self.host_hiv_stat, str):
            self.host_hiv_stat = str(self.host_hiv_stat)

        if self.drug_usage is not None and not isinstance(self.drug_usage, str):
            self.drug_usage = str(self.drug_usage)

        if self.host_body_mass_index is not None and not isinstance(self.host_body_mass_index, str):
            self.host_body_mass_index = str(self.host_body_mass_index)

        if self.diet_last_six_month is not None and not isinstance(self.diet_last_six_month, str):
            self.diet_last_six_month = str(self.diet_last_six_month)

        if self.weight_loss_3_month is not None and not isinstance(self.weight_loss_3_month, str):
            self.weight_loss_3_month = str(self.weight_loss_3_month)

        if self.ihmc_ethnicity is not None and not isinstance(self.ihmc_ethnicity, str):
            self.ihmc_ethnicity = str(self.ihmc_ethnicity)

        if self.host_occupation is not None and not isinstance(self.host_occupation, str):
            self.host_occupation = str(self.host_occupation)

        if self.pet_farm_animal is not None and not isinstance(self.pet_farm_animal, str):
            self.pet_farm_animal = str(self.pet_farm_animal)

        if self.travel_out_six_month is not None and not isinstance(self.travel_out_six_month, str):
            self.travel_out_six_month = str(self.travel_out_six_month)

        if self.twin_sibling is not None and not isinstance(self.twin_sibling, str):
            self.twin_sibling = str(self.twin_sibling)

        if self.medic_hist_perform is not None and not isinstance(self.medic_hist_perform, str):
            self.medic_hist_perform = str(self.medic_hist_perform)

        if self.study_complt_stat is not None and not isinstance(self.study_complt_stat, str):
            self.study_complt_stat = str(self.study_complt_stat)

        if self.pulmonary_disord is not None and not isinstance(self.pulmonary_disord, str):
            self.pulmonary_disord = str(self.pulmonary_disord)

        if self.nose_throat_disord is not None and not isinstance(self.nose_throat_disord, str):
            self.nose_throat_disord = str(self.nose_throat_disord)

        if self.blood_blood_disord is not None and not isinstance(self.blood_blood_disord, str):
            self.blood_blood_disord = str(self.blood_blood_disord)

        if self.host_pulse is not None and not isinstance(self.host_pulse, str):
            self.host_pulse = str(self.host_pulse)

        if self.gestation_state is not None and not isinstance(self.gestation_state, str):
            self.gestation_state = str(self.gestation_state)

        if self.maternal_health_stat is not None and not isinstance(self.maternal_health_stat, str):
            self.maternal_health_stat = str(self.maternal_health_stat)

        if self.foetal_health_stat is not None and not isinstance(self.foetal_health_stat, str):
            self.foetal_health_stat = str(self.foetal_health_stat)

        if self.amniotic_fluid_color is not None and not isinstance(self.amniotic_fluid_color, str):
            self.amniotic_fluid_color = str(self.amniotic_fluid_color)

        if self.urogenit_tract_disor is not None and not isinstance(self.urogenit_tract_disor, str):
            self.urogenit_tract_disor = str(self.urogenit_tract_disor)

        if self.urine_collect_meth is not None and not isinstance(self.urine_collect_meth, str):
            self.urine_collect_meth = str(self.urine_collect_meth)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        super().__post_init__(**kwargs)


@dataclass
class Human-gut(YAMLRoot):
    """
    human-gut
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB["Human-gut"]
    class_class_curie: ClassVar[str] = "mixs.vocab:Human-gut"
    class_name: ClassVar[str] = "human-gut"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Human-gut

    gastrointest_disord: Optional[str] = None
    liver_disord: Optional[str] = None
    special_diet: Optional[str] = None
    host_subject_id: Optional[str] = None
    host_age: Optional[str] = None
    host_sex: Optional[str] = None
    host_disease_stat: Optional[str] = None
    ihmc_medication_code: Optional[str] = None
    chem_administration: Optional[str] = None
    host_body_site: Optional[str] = None
    host_body_product: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_height: Optional[str] = None
    host_diet: Optional[str] = None
    host_last_meal: Optional[str] = None
    host_family_relationship: Optional[str] = None
    host_genotype: Optional[str] = None
    host_phenotype: Optional[str] = None
    host_body_temp: Optional[str] = None
    host_body_mass_index: Optional[str] = None
    ihmc_ethnicity: Optional[str] = None
    host_occupation: Optional[str] = None
    medic_hist_perform: Optional[str] = None
    host_pulse: Optional[str] = None
    perturbation: Optional[str] = None
    samp_salinity: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    temp: Optional[str] = None
    organism_count: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    misc_param: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gastrointest_disord is not None and not isinstance(self.gastrointest_disord, str):
            self.gastrointest_disord = str(self.gastrointest_disord)

        if self.liver_disord is not None and not isinstance(self.liver_disord, str):
            self.liver_disord = str(self.liver_disord)

        if self.special_diet is not None and not isinstance(self.special_diet, str):
            self.special_diet = str(self.special_diet)

        if self.host_subject_id is not None and not isinstance(self.host_subject_id, str):
            self.host_subject_id = str(self.host_subject_id)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_sex is not None and not isinstance(self.host_sex, str):
            self.host_sex = str(self.host_sex)

        if self.host_disease_stat is not None and not isinstance(self.host_disease_stat, str):
            self.host_disease_stat = str(self.host_disease_stat)

        if self.ihmc_medication_code is not None and not isinstance(self.ihmc_medication_code, str):
            self.ihmc_medication_code = str(self.ihmc_medication_code)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.host_body_site is not None and not isinstance(self.host_body_site, str):
            self.host_body_site = str(self.host_body_site)

        if self.host_body_product is not None and not isinstance(self.host_body_product, str):
            self.host_body_product = str(self.host_body_product)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_diet is not None and not isinstance(self.host_diet, str):
            self.host_diet = str(self.host_diet)

        if self.host_last_meal is not None and not isinstance(self.host_last_meal, str):
            self.host_last_meal = str(self.host_last_meal)

        if self.host_family_relationship is not None and not isinstance(self.host_family_relationship, str):
            self.host_family_relationship = str(self.host_family_relationship)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if self.host_body_temp is not None and not isinstance(self.host_body_temp, str):
            self.host_body_temp = str(self.host_body_temp)

        if self.host_body_mass_index is not None and not isinstance(self.host_body_mass_index, str):
            self.host_body_mass_index = str(self.host_body_mass_index)

        if self.ihmc_ethnicity is not None and not isinstance(self.ihmc_ethnicity, str):
            self.ihmc_ethnicity = str(self.ihmc_ethnicity)

        if self.host_occupation is not None and not isinstance(self.host_occupation, str):
            self.host_occupation = str(self.host_occupation)

        if self.medic_hist_perform is not None and not isinstance(self.medic_hist_perform, str):
            self.medic_hist_perform = str(self.medic_hist_perform)

        if self.host_pulse is not None and not isinstance(self.host_pulse, str):
            self.host_pulse = str(self.host_pulse)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        super().__post_init__(**kwargs)


@dataclass
class Human-oral(YAMLRoot):
    """
    human-oral
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB["Human-oral"]
    class_class_curie: ClassVar[str] = "mixs.vocab:Human-oral"
    class_name: ClassVar[str] = "human-oral"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Human-oral

    nose_mouth_teeth_throat_disord: Optional[str] = None
    time_last_toothbrush: Optional[str] = None
    host_subject_id: Optional[str] = None
    host_age: Optional[str] = None
    host_sex: Optional[str] = None
    host_disease_stat: Optional[str] = None
    ihmc_medication_code: Optional[str] = None
    chem_administration: Optional[str] = None
    host_body_site: Optional[str] = None
    host_body_product: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_height: Optional[str] = None
    host_diet: Optional[str] = None
    host_last_meal: Optional[str] = None
    host_family_relationship: Optional[str] = None
    host_genotype: Optional[str] = None
    host_phenotype: Optional[str] = None
    host_body_temp: Optional[str] = None
    host_body_mass_index: Optional[str] = None
    ihmc_ethnicity: Optional[str] = None
    host_occupation: Optional[str] = None
    medic_hist_perform: Optional[str] = None
    host_pulse: Optional[str] = None
    perturbation: Optional[str] = None
    samp_salinity: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    temp: Optional[str] = None
    organism_count: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    misc_param: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.nose_mouth_teeth_throat_disord is not None and not isinstance(self.nose_mouth_teeth_throat_disord, str):
            self.nose_mouth_teeth_throat_disord = str(self.nose_mouth_teeth_throat_disord)

        if self.time_last_toothbrush is not None and not isinstance(self.time_last_toothbrush, str):
            self.time_last_toothbrush = str(self.time_last_toothbrush)

        if self.host_subject_id is not None and not isinstance(self.host_subject_id, str):
            self.host_subject_id = str(self.host_subject_id)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_sex is not None and not isinstance(self.host_sex, str):
            self.host_sex = str(self.host_sex)

        if self.host_disease_stat is not None and not isinstance(self.host_disease_stat, str):
            self.host_disease_stat = str(self.host_disease_stat)

        if self.ihmc_medication_code is not None and not isinstance(self.ihmc_medication_code, str):
            self.ihmc_medication_code = str(self.ihmc_medication_code)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.host_body_site is not None and not isinstance(self.host_body_site, str):
            self.host_body_site = str(self.host_body_site)

        if self.host_body_product is not None and not isinstance(self.host_body_product, str):
            self.host_body_product = str(self.host_body_product)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_diet is not None and not isinstance(self.host_diet, str):
            self.host_diet = str(self.host_diet)

        if self.host_last_meal is not None and not isinstance(self.host_last_meal, str):
            self.host_last_meal = str(self.host_last_meal)

        if self.host_family_relationship is not None and not isinstance(self.host_family_relationship, str):
            self.host_family_relationship = str(self.host_family_relationship)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if self.host_body_temp is not None and not isinstance(self.host_body_temp, str):
            self.host_body_temp = str(self.host_body_temp)

        if self.host_body_mass_index is not None and not isinstance(self.host_body_mass_index, str):
            self.host_body_mass_index = str(self.host_body_mass_index)

        if self.ihmc_ethnicity is not None and not isinstance(self.ihmc_ethnicity, str):
            self.ihmc_ethnicity = str(self.ihmc_ethnicity)

        if self.host_occupation is not None and not isinstance(self.host_occupation, str):
            self.host_occupation = str(self.host_occupation)

        if self.medic_hist_perform is not None and not isinstance(self.medic_hist_perform, str):
            self.medic_hist_perform = str(self.medic_hist_perform)

        if self.host_pulse is not None and not isinstance(self.host_pulse, str):
            self.host_pulse = str(self.host_pulse)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        super().__post_init__(**kwargs)


@dataclass
class Human-skin(YAMLRoot):
    """
    human-skin
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB["Human-skin"]
    class_class_curie: ClassVar[str] = "mixs.vocab:Human-skin"
    class_name: ClassVar[str] = "human-skin"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Human-skin

    dermatology_disord: Optional[str] = None
    time_since_last_wash: Optional[str] = None
    dominant_hand: Optional[str] = None
    host_subject_id: Optional[str] = None
    host_age: Optional[str] = None
    host_sex: Optional[str] = None
    host_disease_stat: Optional[str] = None
    ihmc_medication_code: Optional[str] = None
    chem_administration: Optional[str] = None
    host_body_site: Optional[str] = None
    host_body_product: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_height: Optional[str] = None
    host_diet: Optional[str] = None
    host_last_meal: Optional[str] = None
    host_family_relationship: Optional[str] = None
    host_genotype: Optional[str] = None
    host_phenotype: Optional[str] = None
    host_body_temp: Optional[str] = None
    host_body_mass_index: Optional[str] = None
    ihmc_ethnicity: Optional[str] = None
    host_occupation: Optional[str] = None
    medic_hist_perform: Optional[str] = None
    host_pulse: Optional[str] = None
    perturbation: Optional[str] = None
    samp_salinity: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    temp: Optional[str] = None
    organism_count: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    misc_param: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dermatology_disord is not None and not isinstance(self.dermatology_disord, str):
            self.dermatology_disord = str(self.dermatology_disord)

        if self.time_since_last_wash is not None and not isinstance(self.time_since_last_wash, str):
            self.time_since_last_wash = str(self.time_since_last_wash)

        if self.dominant_hand is not None and not isinstance(self.dominant_hand, str):
            self.dominant_hand = str(self.dominant_hand)

        if self.host_subject_id is not None and not isinstance(self.host_subject_id, str):
            self.host_subject_id = str(self.host_subject_id)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_sex is not None and not isinstance(self.host_sex, str):
            self.host_sex = str(self.host_sex)

        if self.host_disease_stat is not None and not isinstance(self.host_disease_stat, str):
            self.host_disease_stat = str(self.host_disease_stat)

        if self.ihmc_medication_code is not None and not isinstance(self.ihmc_medication_code, str):
            self.ihmc_medication_code = str(self.ihmc_medication_code)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.host_body_site is not None and not isinstance(self.host_body_site, str):
            self.host_body_site = str(self.host_body_site)

        if self.host_body_product is not None and not isinstance(self.host_body_product, str):
            self.host_body_product = str(self.host_body_product)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_diet is not None and not isinstance(self.host_diet, str):
            self.host_diet = str(self.host_diet)

        if self.host_last_meal is not None and not isinstance(self.host_last_meal, str):
            self.host_last_meal = str(self.host_last_meal)

        if self.host_family_relationship is not None and not isinstance(self.host_family_relationship, str):
            self.host_family_relationship = str(self.host_family_relationship)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if self.host_body_temp is not None and not isinstance(self.host_body_temp, str):
            self.host_body_temp = str(self.host_body_temp)

        if self.host_body_mass_index is not None and not isinstance(self.host_body_mass_index, str):
            self.host_body_mass_index = str(self.host_body_mass_index)

        if self.ihmc_ethnicity is not None and not isinstance(self.ihmc_ethnicity, str):
            self.ihmc_ethnicity = str(self.ihmc_ethnicity)

        if self.host_occupation is not None and not isinstance(self.host_occupation, str):
            self.host_occupation = str(self.host_occupation)

        if self.medic_hist_perform is not None and not isinstance(self.medic_hist_perform, str):
            self.medic_hist_perform = str(self.medic_hist_perform)

        if self.host_pulse is not None and not isinstance(self.host_pulse, str):
            self.host_pulse = str(self.host_pulse)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        super().__post_init__(**kwargs)


@dataclass
class Human-vaginal(YAMLRoot):
    """
    human-vaginal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB["Human-vaginal"]
    class_class_curie: ClassVar[str] = "mixs.vocab:Human-vaginal"
    class_name: ClassVar[str] = "human-vaginal"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Human-vaginal

    menarche: Optional[str] = None
    sexual_act: Optional[str] = None
    pregnancy: Optional[str] = None
    douche: Optional[str] = None
    birth_control: Optional[str] = None
    menopause: Optional[str] = None
    hrt: Optional[str] = None
    hysterectomy: Optional[str] = None
    gynecologic_disord: Optional[str] = None
    urogenit_disord: Optional[str] = None
    host_subject_id: Optional[str] = None
    host_age: Optional[str] = None
    host_sex: Optional[str] = None
    host_disease_stat: Optional[str] = None
    ihmc_medication_code: Optional[str] = None
    chem_administration: Optional[str] = None
    host_body_site: Optional[str] = None
    host_body_product: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_height: Optional[str] = None
    host_diet: Optional[str] = None
    host_last_meal: Optional[str] = None
    host_family_relationship: Optional[str] = None
    host_genotype: Optional[str] = None
    host_phenotype: Optional[str] = None
    host_body_temp: Optional[str] = None
    host_body_mass_index: Optional[str] = None
    ihmc_ethnicity: Optional[str] = None
    host_occupation: Optional[str] = None
    medic_hist_perform: Optional[str] = None
    host_pulse: Optional[str] = None
    perturbation: Optional[str] = None
    samp_salinity: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    temp: Optional[str] = None
    organism_count: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_dur: Optional[str] = None
    misc_param: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.menarche is not None and not isinstance(self.menarche, str):
            self.menarche = str(self.menarche)

        if self.sexual_act is not None and not isinstance(self.sexual_act, str):
            self.sexual_act = str(self.sexual_act)

        if self.pregnancy is not None and not isinstance(self.pregnancy, str):
            self.pregnancy = str(self.pregnancy)

        if self.douche is not None and not isinstance(self.douche, str):
            self.douche = str(self.douche)

        if self.birth_control is not None and not isinstance(self.birth_control, str):
            self.birth_control = str(self.birth_control)

        if self.menopause is not None and not isinstance(self.menopause, str):
            self.menopause = str(self.menopause)

        if self.hrt is not None and not isinstance(self.hrt, str):
            self.hrt = str(self.hrt)

        if self.hysterectomy is not None and not isinstance(self.hysterectomy, str):
            self.hysterectomy = str(self.hysterectomy)

        if self.gynecologic_disord is not None and not isinstance(self.gynecologic_disord, str):
            self.gynecologic_disord = str(self.gynecologic_disord)

        if self.urogenit_disord is not None and not isinstance(self.urogenit_disord, str):
            self.urogenit_disord = str(self.urogenit_disord)

        if self.host_subject_id is not None and not isinstance(self.host_subject_id, str):
            self.host_subject_id = str(self.host_subject_id)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_sex is not None and not isinstance(self.host_sex, str):
            self.host_sex = str(self.host_sex)

        if self.host_disease_stat is not None and not isinstance(self.host_disease_stat, str):
            self.host_disease_stat = str(self.host_disease_stat)

        if self.ihmc_medication_code is not None and not isinstance(self.ihmc_medication_code, str):
            self.ihmc_medication_code = str(self.ihmc_medication_code)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.host_body_site is not None and not isinstance(self.host_body_site, str):
            self.host_body_site = str(self.host_body_site)

        if self.host_body_product is not None and not isinstance(self.host_body_product, str):
            self.host_body_product = str(self.host_body_product)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_diet is not None and not isinstance(self.host_diet, str):
            self.host_diet = str(self.host_diet)

        if self.host_last_meal is not None and not isinstance(self.host_last_meal, str):
            self.host_last_meal = str(self.host_last_meal)

        if self.host_family_relationship is not None and not isinstance(self.host_family_relationship, str):
            self.host_family_relationship = str(self.host_family_relationship)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if self.host_body_temp is not None and not isinstance(self.host_body_temp, str):
            self.host_body_temp = str(self.host_body_temp)

        if self.host_body_mass_index is not None and not isinstance(self.host_body_mass_index, str):
            self.host_body_mass_index = str(self.host_body_mass_index)

        if self.ihmc_ethnicity is not None and not isinstance(self.ihmc_ethnicity, str):
            self.ihmc_ethnicity = str(self.ihmc_ethnicity)

        if self.host_occupation is not None and not isinstance(self.host_occupation, str):
            self.host_occupation = str(self.host_occupation)

        if self.medic_hist_perform is not None and not isinstance(self.medic_hist_perform, str):
            self.medic_hist_perform = str(self.medic_hist_perform)

        if self.host_pulse is not None and not isinstance(self.host_pulse, str):
            self.host_pulse = str(self.host_pulse)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        super().__post_init__(**kwargs)


@dataclass
class HydrocarbonResources-cores(YAMLRoot):
    """
    hydrocarbon resources-cores
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB["HydrocarbonResources-cores"]
    class_class_curie: ClassVar[str] = "mixs.vocab:HydrocarbonResources-cores"
    class_name: ClassVar[str] = "hydrocarbon resources-cores"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.HydrocarbonResources-cores

    hcr: Optional[str] = None
    hc_produced: Optional[str] = None
    basin: Optional[str] = None
    field: Optional[str] = None
    reservoir: Optional[str] = None
    hcr_temp: Optional[str] = None
    tvdss_of_hcr_temp: Optional[str] = None
    hcr_pressure: Optional[str] = None
    tvdss_of_hcr_pressure: Optional[str] = None
    permeability: Optional[str] = None
    porosity: Optional[str] = None
    lithology: Optional[str] = None
    depos_env: Optional[str] = None
    hcr_geol_age: Optional[str] = None
    owc_tvdss: Optional[str] = None
    hcr_fw_salinity: Optional[str] = None
    sulfate_fw: Optional[str] = None
    vfa_fw: Optional[str] = None
    sr_kerog_type: Optional[str] = None
    sr_lithology: Optional[str] = None
    sr_dep_env: Optional[str] = None
    sr_geol_age: Optional[str] = None
    samp_well_name: Optional[str] = None
    win: Optional[str] = None
    samp_type: Optional[str] = None
    samp_subtype: Optional[str] = None
    temp: Optional[str] = None
    pressure: Optional[str] = None
    samp_tvdss: Optional[str] = None
    samp_md: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    samp_transport_cond: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    organism_count: Optional[str] = None
    organism_count_qpcr_info: Optional[str] = None
    ph: Optional[str] = None
    samp_salinity: Optional[str] = None
    alkalinity: Optional[str] = None
    alkalinity_method: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    tot_sulfur: Optional[str] = None
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    ammonium: Optional[str] = None
    tot_nitro: Optional[str] = None
    diss_iron: Optional[str] = None
    sodium: Optional[str] = None
    chloride: Optional[str] = None
    potassium: Optional[str] = None
    magnesium: Optional[str] = None
    calcium: Optional[str] = None
    tot_iron: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_inorg_phosp: Optional[str] = None
    tot_phosp: Optional[str] = None
    suspend_solids: Optional[str] = None
    density: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_oxygen_fluid: Optional[str] = None
    vfa: Optional[str] = None
    benzene: Optional[str] = None
    toluene: Optional[str] = None
    ethylbenzene: Optional[str] = None
    xylene: Optional[str] = None
    api: Optional[str] = None
    tan: Optional[str] = None
    viscosity: Optional[str] = None
    pour_point: Optional[str] = None
    saturates_pc: Optional[str] = None
    aromatics_pc: Optional[str] = None
    resins_pc: Optional[str] = None
    asphaltenes_pc: Optional[str] = None
    misc_param: Optional[str] = None
    additional_info: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hcr is not None and not isinstance(self.hcr, str):
            self.hcr = str(self.hcr)

        if self.hc_produced is not None and not isinstance(self.hc_produced, str):
            self.hc_produced = str(self.hc_produced)

        if self.basin is not None and not isinstance(self.basin, str):
            self.basin = str(self.basin)

        if self.field is not None and not isinstance(self.field, str):
            self.field = str(self.field)

        if self.reservoir is not None and not isinstance(self.reservoir, str):
            self.reservoir = str(self.reservoir)

        if self.hcr_temp is not None and not isinstance(self.hcr_temp, str):
            self.hcr_temp = str(self.hcr_temp)

        if self.tvdss_of_hcr_temp is not None and not isinstance(self.tvdss_of_hcr_temp, str):
            self.tvdss_of_hcr_temp = str(self.tvdss_of_hcr_temp)

        if self.hcr_pressure is not None and not isinstance(self.hcr_pressure, str):
            self.hcr_pressure = str(self.hcr_pressure)

        if self.tvdss_of_hcr_pressure is not None and not isinstance(self.tvdss_of_hcr_pressure, str):
            self.tvdss_of_hcr_pressure = str(self.tvdss_of_hcr_pressure)

        if self.permeability is not None and not isinstance(self.permeability, str):
            self.permeability = str(self.permeability)

        if self.porosity is not None and not isinstance(self.porosity, str):
            self.porosity = str(self.porosity)

        if self.lithology is not None and not isinstance(self.lithology, str):
            self.lithology = str(self.lithology)

        if self.depos_env is not None and not isinstance(self.depos_env, str):
            self.depos_env = str(self.depos_env)

        if self.hcr_geol_age is not None and not isinstance(self.hcr_geol_age, str):
            self.hcr_geol_age = str(self.hcr_geol_age)

        if self.owc_tvdss is not None and not isinstance(self.owc_tvdss, str):
            self.owc_tvdss = str(self.owc_tvdss)

        if self.hcr_fw_salinity is not None and not isinstance(self.hcr_fw_salinity, str):
            self.hcr_fw_salinity = str(self.hcr_fw_salinity)

        if self.sulfate_fw is not None and not isinstance(self.sulfate_fw, str):
            self.sulfate_fw = str(self.sulfate_fw)

        if self.vfa_fw is not None and not isinstance(self.vfa_fw, str):
            self.vfa_fw = str(self.vfa_fw)

        if self.sr_kerog_type is not None and not isinstance(self.sr_kerog_type, str):
            self.sr_kerog_type = str(self.sr_kerog_type)

        if self.sr_lithology is not None and not isinstance(self.sr_lithology, str):
            self.sr_lithology = str(self.sr_lithology)

        if self.sr_dep_env is not None and not isinstance(self.sr_dep_env, str):
            self.sr_dep_env = str(self.sr_dep_env)

        if self.sr_geol_age is not None and not isinstance(self.sr_geol_age, str):
            self.sr_geol_age = str(self.sr_geol_age)

        if self.samp_well_name is not None and not isinstance(self.samp_well_name, str):
            self.samp_well_name = str(self.samp_well_name)

        if self.win is not None and not isinstance(self.win, str):
            self.win = str(self.win)

        if self.samp_type is not None and not isinstance(self.samp_type, str):
            self.samp_type = str(self.samp_type)

        if self.samp_subtype is not None and not isinstance(self.samp_subtype, str):
            self.samp_subtype = str(self.samp_subtype)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.samp_tvdss is not None and not isinstance(self.samp_tvdss, str):
            self.samp_tvdss = str(self.samp_tvdss)

        if self.samp_md is not None and not isinstance(self.samp_md, str):
            self.samp_md = str(self.samp_md)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.samp_transport_cond is not None and not isinstance(self.samp_transport_cond, str):
            self.samp_transport_cond = str(self.samp_transport_cond)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.organism_count_qpcr_info is not None and not isinstance(self.organism_count_qpcr_info, str):
            self.organism_count_qpcr_info = str(self.organism_count_qpcr_info)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.tot_sulfur is not None and not isinstance(self.tot_sulfur, str):
            self.tot_sulfur = str(self.tot_sulfur)

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.diss_iron is not None and not isinstance(self.diss_iron, str):
            self.diss_iron = str(self.diss_iron)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.tot_iron is not None and not isinstance(self.tot_iron, str):
            self.tot_iron = str(self.tot_iron)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.suspend_solids is not None and not isinstance(self.suspend_solids, str):
            self.suspend_solids = str(self.suspend_solids)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_oxygen_fluid is not None and not isinstance(self.diss_oxygen_fluid, str):
            self.diss_oxygen_fluid = str(self.diss_oxygen_fluid)

        if self.vfa is not None and not isinstance(self.vfa, str):
            self.vfa = str(self.vfa)

        if self.benzene is not None and not isinstance(self.benzene, str):
            self.benzene = str(self.benzene)

        if self.toluene is not None and not isinstance(self.toluene, str):
            self.toluene = str(self.toluene)

        if self.ethylbenzene is not None and not isinstance(self.ethylbenzene, str):
            self.ethylbenzene = str(self.ethylbenzene)

        if self.xylene is not None and not isinstance(self.xylene, str):
            self.xylene = str(self.xylene)

        if self.api is not None and not isinstance(self.api, str):
            self.api = str(self.api)

        if self.tan is not None and not isinstance(self.tan, str):
            self.tan = str(self.tan)

        if self.viscosity is not None and not isinstance(self.viscosity, str):
            self.viscosity = str(self.viscosity)

        if self.pour_point is not None and not isinstance(self.pour_point, str):
            self.pour_point = str(self.pour_point)

        if self.saturates_pc is not None and not isinstance(self.saturates_pc, str):
            self.saturates_pc = str(self.saturates_pc)

        if self.aromatics_pc is not None and not isinstance(self.aromatics_pc, str):
            self.aromatics_pc = str(self.aromatics_pc)

        if self.resins_pc is not None and not isinstance(self.resins_pc, str):
            self.resins_pc = str(self.resins_pc)

        if self.asphaltenes_pc is not None and not isinstance(self.asphaltenes_pc, str):
            self.asphaltenes_pc = str(self.asphaltenes_pc)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.additional_info is not None and not isinstance(self.additional_info, str):
            self.additional_info = str(self.additional_info)

        super().__post_init__(**kwargs)


@dataclass
class HydrocarbonResources-fluidsSwabs(YAMLRoot):
    """
    hydrocarbon resources-fluids/swabs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB["HydrocarbonResources-fluidsSwabs"]
    class_class_curie: ClassVar[str] = "mixs.vocab:HydrocarbonResources-fluidsSwabs"
    class_name: ClassVar[str] = "hydrocarbon resources-fluids_swabs"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.HydrocarbonResources-fluidsSwabs

    hcr: Optional[str] = None
    hc_produced: Optional[str] = None
    basin: Optional[str] = None
    field: Optional[str] = None
    reservoir: Optional[str] = None
    hcr_temp: Optional[str] = None
    tvdss_of_hcr_temp: Optional[str] = None
    hcr_pressure: Optional[str] = None
    tvdss_of_hcr_pressure: Optional[str] = None
    lithology: Optional[str] = None
    depos_env: Optional[str] = None
    hcr_geol_age: Optional[str] = None
    hcr_fw_salinity: Optional[str] = None
    sulfate_fw: Optional[str] = None
    vfa_fw: Optional[str] = None
    prod_start_date: Optional[str] = None
    prod_rate: Optional[str] = None
    water_production_rate: Optional[str] = None
    water_cut: Optional[str] = None
    iwf: Optional[str] = None
    add_recov_method: Optional[str] = None
    iw_bt_date_well: Optional[str] = None
    biocide: Optional[str] = None
    biocide_admin_method: Optional[str] = None
    chem_treatment: Optional[str] = None
    chem_treatment_method: Optional[str] = None
    samp_loc_corr_rate: Optional[str] = None
    samp_well_name: Optional[str] = None
    win: Optional[str] = None
    samp_type: Optional[str] = None
    samp_subtype: Optional[str] = None
    samp_collection_point: Optional[str] = None
    temp: Optional[str] = None
    pressure: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    samp_preserv: Optional[str] = None
    samp_transport_cond: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    organism_count: Optional[str] = None
    organism_count_qpcr_info: Optional[str] = None
    ph: Optional[str] = None
    samp_salinity: Optional[str] = None
    alkalinity: Optional[str] = None
    alkalinity_method: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    tot_sulfur: Optional[str] = None
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    ammonium: Optional[str] = None
    tot_nitro: Optional[str] = None
    diss_iron: Optional[str] = None
    sodium: Optional[str] = None
    chloride: Optional[str] = None
    potassium: Optional[str] = None
    magnesium: Optional[str] = None
    calcium: Optional[str] = None
    tot_iron: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_inorg_phosp: Optional[str] = None
    tot_phosp: Optional[str] = None
    suspend_solids: Optional[str] = None
    density: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_oxygen_fluid: Optional[str] = None
    vfa: Optional[str] = None
    benzene: Optional[str] = None
    toluene: Optional[str] = None
    ethylbenzene: Optional[str] = None
    xylene: Optional[str] = None
    api: Optional[str] = None
    tan: Optional[str] = None
    viscosity: Optional[str] = None
    pour_point: Optional[str] = None
    saturates_pc: Optional[str] = None
    aromatics_pc: Optional[str] = None
    resins_pc: Optional[str] = None
    asphaltenes_pc: Optional[str] = None
    misc_param: Optional[str] = None
    additional_info: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hcr is not None and not isinstance(self.hcr, str):
            self.hcr = str(self.hcr)

        if self.hc_produced is not None and not isinstance(self.hc_produced, str):
            self.hc_produced = str(self.hc_produced)

        if self.basin is not None and not isinstance(self.basin, str):
            self.basin = str(self.basin)

        if self.field is not None and not isinstance(self.field, str):
            self.field = str(self.field)

        if self.reservoir is not None and not isinstance(self.reservoir, str):
            self.reservoir = str(self.reservoir)

        if self.hcr_temp is not None and not isinstance(self.hcr_temp, str):
            self.hcr_temp = str(self.hcr_temp)

        if self.tvdss_of_hcr_temp is not None and not isinstance(self.tvdss_of_hcr_temp, str):
            self.tvdss_of_hcr_temp = str(self.tvdss_of_hcr_temp)

        if self.hcr_pressure is not None and not isinstance(self.hcr_pressure, str):
            self.hcr_pressure = str(self.hcr_pressure)

        if self.tvdss_of_hcr_pressure is not None and not isinstance(self.tvdss_of_hcr_pressure, str):
            self.tvdss_of_hcr_pressure = str(self.tvdss_of_hcr_pressure)

        if self.lithology is not None and not isinstance(self.lithology, str):
            self.lithology = str(self.lithology)

        if self.depos_env is not None and not isinstance(self.depos_env, str):
            self.depos_env = str(self.depos_env)

        if self.hcr_geol_age is not None and not isinstance(self.hcr_geol_age, str):
            self.hcr_geol_age = str(self.hcr_geol_age)

        if self.hcr_fw_salinity is not None and not isinstance(self.hcr_fw_salinity, str):
            self.hcr_fw_salinity = str(self.hcr_fw_salinity)

        if self.sulfate_fw is not None and not isinstance(self.sulfate_fw, str):
            self.sulfate_fw = str(self.sulfate_fw)

        if self.vfa_fw is not None and not isinstance(self.vfa_fw, str):
            self.vfa_fw = str(self.vfa_fw)

        if self.prod_start_date is not None and not isinstance(self.prod_start_date, str):
            self.prod_start_date = str(self.prod_start_date)

        if self.prod_rate is not None and not isinstance(self.prod_rate, str):
            self.prod_rate = str(self.prod_rate)

        if self.water_production_rate is not None and not isinstance(self.water_production_rate, str):
            self.water_production_rate = str(self.water_production_rate)

        if self.water_cut is not None and not isinstance(self.water_cut, str):
            self.water_cut = str(self.water_cut)

        if self.iwf is not None and not isinstance(self.iwf, str):
            self.iwf = str(self.iwf)

        if self.add_recov_method is not None and not isinstance(self.add_recov_method, str):
            self.add_recov_method = str(self.add_recov_method)

        if self.iw_bt_date_well is not None and not isinstance(self.iw_bt_date_well, str):
            self.iw_bt_date_well = str(self.iw_bt_date_well)

        if self.biocide is not None and not isinstance(self.biocide, str):
            self.biocide = str(self.biocide)

        if self.biocide_admin_method is not None and not isinstance(self.biocide_admin_method, str):
            self.biocide_admin_method = str(self.biocide_admin_method)

        if self.chem_treatment is not None and not isinstance(self.chem_treatment, str):
            self.chem_treatment = str(self.chem_treatment)

        if self.chem_treatment_method is not None and not isinstance(self.chem_treatment_method, str):
            self.chem_treatment_method = str(self.chem_treatment_method)

        if self.samp_loc_corr_rate is not None and not isinstance(self.samp_loc_corr_rate, str):
            self.samp_loc_corr_rate = str(self.samp_loc_corr_rate)

        if self.samp_well_name is not None and not isinstance(self.samp_well_name, str):
            self.samp_well_name = str(self.samp_well_name)

        if self.win is not None and not isinstance(self.win, str):
            self.win = str(self.win)

        if self.samp_type is not None and not isinstance(self.samp_type, str):
            self.samp_type = str(self.samp_type)

        if self.samp_subtype is not None and not isinstance(self.samp_subtype, str):
            self.samp_subtype = str(self.samp_subtype)

        if self.samp_collection_point is not None and not isinstance(self.samp_collection_point, str):
            self.samp_collection_point = str(self.samp_collection_point)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.samp_preserv is not None and not isinstance(self.samp_preserv, str):
            self.samp_preserv = str(self.samp_preserv)

        if self.samp_transport_cond is not None and not isinstance(self.samp_transport_cond, str):
            self.samp_transport_cond = str(self.samp_transport_cond)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.organism_count_qpcr_info is not None and not isinstance(self.organism_count_qpcr_info, str):
            self.organism_count_qpcr_info = str(self.organism_count_qpcr_info)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.tot_sulfur is not None and not isinstance(self.tot_sulfur, str):
            self.tot_sulfur = str(self.tot_sulfur)

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.diss_iron is not None and not isinstance(self.diss_iron, str):
            self.diss_iron = str(self.diss_iron)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.tot_iron is not None and not isinstance(self.tot_iron, str):
            self.tot_iron = str(self.tot_iron)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.suspend_solids is not None and not isinstance(self.suspend_solids, str):
            self.suspend_solids = str(self.suspend_solids)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_oxygen_fluid is not None and not isinstance(self.diss_oxygen_fluid, str):
            self.diss_oxygen_fluid = str(self.diss_oxygen_fluid)

        if self.vfa is not None and not isinstance(self.vfa, str):
            self.vfa = str(self.vfa)

        if self.benzene is not None and not isinstance(self.benzene, str):
            self.benzene = str(self.benzene)

        if self.toluene is not None and not isinstance(self.toluene, str):
            self.toluene = str(self.toluene)

        if self.ethylbenzene is not None and not isinstance(self.ethylbenzene, str):
            self.ethylbenzene = str(self.ethylbenzene)

        if self.xylene is not None and not isinstance(self.xylene, str):
            self.xylene = str(self.xylene)

        if self.api is not None and not isinstance(self.api, str):
            self.api = str(self.api)

        if self.tan is not None and not isinstance(self.tan, str):
            self.tan = str(self.tan)

        if self.viscosity is not None and not isinstance(self.viscosity, str):
            self.viscosity = str(self.viscosity)

        if self.pour_point is not None and not isinstance(self.pour_point, str):
            self.pour_point = str(self.pour_point)

        if self.saturates_pc is not None and not isinstance(self.saturates_pc, str):
            self.saturates_pc = str(self.saturates_pc)

        if self.aromatics_pc is not None and not isinstance(self.aromatics_pc, str):
            self.aromatics_pc = str(self.aromatics_pc)

        if self.resins_pc is not None and not isinstance(self.resins_pc, str):
            self.resins_pc = str(self.resins_pc)

        if self.asphaltenes_pc is not None and not isinstance(self.asphaltenes_pc, str):
            self.asphaltenes_pc = str(self.asphaltenes_pc)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.additional_info is not None and not isinstance(self.additional_info, str):
            self.additional_info = str(self.additional_info)

        super().__post_init__(**kwargs)


@dataclass
class MicrobialMatBiofilm(YAMLRoot):
    """
    microbial mat/biofilm
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB.MicrobialMatBiofilm
    class_class_curie: ClassVar[str] = "mixs.vocab:MicrobialMatBiofilm"
    class_name: ClassVar[str] = "microbial mat_biofilm"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.MicrobialMatBiofilm

    alkalinity: Optional[str] = None
    alkyl_diethers: Optional[str] = None
    aminopept_act: Optional[str] = None
    ammonium: Optional[str] = None
    bacteria_carb_prod: Optional[str] = None
    biomass: Optional[str] = None
    bishomohopanol: Optional[str] = None
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[str] = None
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    diether_lipids: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    glucosidase_act: Optional[str] = None
    magnesium: Optional[str] = None
    mean_frict_vel: Optional[str] = None
    mean_peak_frict_vel: Optional[str] = None
    methane: Optional[str] = None
    misc_param: Optional[str] = None
    n_alkanes: Optional[str] = None
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    organism_count: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    ph: Optional[str] = None
    part_org_carb: Optional[str] = None
    perturbation: Optional[str] = None
    petroleum_hydrocarb: Optional[str] = None
    phaeopigments: Optional[str] = None
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[str] = None
    potassium: Optional[str] = None
    pressure: Optional[str] = None
    redox_potential: Optional[str] = None
    salinity: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    silicate: Optional[str] = None
    sodium: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    temp: Optional[str] = None
    tot_carb: Optional[str] = None
    tot_nitro_content: Optional[str] = None
    tot_org_carb: Optional[str] = None
    turbidity: Optional[str] = None
    water_content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if self.biomass is not None and not isinstance(self.biomass, str):
            self.biomass = str(self.biomass)

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.diether_lipids is not None and not isinstance(self.diether_lipids, str):
            self.diether_lipids = str(self.diether_lipids)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.n_alkanes is not None and not isinstance(self.n_alkanes, str):
            self.n_alkanes = str(self.n_alkanes)

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.phaeopigments is not None and not isinstance(self.phaeopigments, str):
            self.phaeopigments = str(self.phaeopigments)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.phosplipid_fatt_acid is not None and not isinstance(self.phosplipid_fatt_acid, str):
            self.phosplipid_fatt_acid = str(self.phosplipid_fatt_acid)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        super().__post_init__(**kwargs)


@dataclass
class MiscellaneousNaturalOrArtificialEnvironment(YAMLRoot):
    """
    miscellaneous natural or artificial environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB.MiscellaneousNaturalOrArtificialEnvironment
    class_class_curie: ClassVar[str] = "mixs.vocab:MiscellaneousNaturalOrArtificialEnvironment"
    class_name: ClassVar[str] = "miscellaneous natural or artificial environment"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.MiscellaneousNaturalOrArtificialEnvironment

    alkalinity: Optional[str] = None
    ammonium: Optional[str] = None
    biomass: Optional[str] = None
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    chem_administration: Optional[str] = None
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    density: Optional[str] = None
    diether_lipids: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    misc_param: Optional[str] = None
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    organism_count: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    ph: Optional[str] = None
    perturbation: Optional[str] = None
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[str] = None
    potassium: Optional[str] = None
    pressure: Optional[str] = None
    salinity: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    silicate: Optional[str] = None
    sodium: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    temp: Optional[str] = None
    water_current: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.biomass is not None and not isinstance(self.biomass, str):
            self.biomass = str(self.biomass)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.diether_lipids is not None and not isinstance(self.diether_lipids, str):
            self.diether_lipids = str(self.diether_lipids)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.phosplipid_fatt_acid is not None and not isinstance(self.phosplipid_fatt_acid, str):
            self.phosplipid_fatt_acid = str(self.phosplipid_fatt_acid)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.water_current is not None and not isinstance(self.water_current, str):
            self.water_current = str(self.water_current)

        super().__post_init__(**kwargs)


@dataclass
class Plant-associated(YAMLRoot):
    """
    plant-associated
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB["Plant-associated"]
    class_class_curie: ClassVar[str] = "mixs.vocab:Plant-associated"
    class_name: ClassVar[str] = "plant-associated"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Plant-associated

    air_temp_regm: Optional[str] = None
    ances_data: Optional[str] = None
    antibiotic_regm: Optional[str] = None
    biol_stat: Optional[str] = None
    biotic_regm: Optional[str] = None
    chem_administration: Optional[str] = None
    chem_mutagen: Optional[str] = None
    climate_environment: Optional[str] = None
    cult_root_med: Optional[str] = None
    fertilizer_regm: Optional[str] = None
    fungicide_regm: Optional[str] = None
    gaseous_environment: Optional[str] = None
    genetic_mod: Optional[str] = None
    gravity: Optional[str] = None
    growth_facil: Optional[str] = None
    growth_habit: Optional[str] = None
    growth_hormone_regm: Optional[str] = None
    herbicide_regm: Optional[str] = None
    host_age: Optional[str] = None
    host_common_name: Optional[str] = None
    host_disease_stat: Optional[str] = None
    host_dry_mass: Optional[str] = None
    host_genotype: Optional[str] = None
    host_height: Optional[str] = None
    host_infra_specific_name: Optional[str] = None
    host_infra_specific_rank: Optional[str] = None
    host_length: Optional[str] = None
    host_life_stage: Optional[str] = None
    host_phenotype: Optional[str] = None
    host_taxid: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_wet_mass: Optional[str] = None
    humidity_regm: Optional[str] = None
    light_regm: Optional[str] = None
    mechanical_damage: Optional[str] = None
    mineral_nutr_regm: Optional[str] = None
    misc_param: Optional[str] = None
    non_mineral_nutr_regm: Optional[str] = None
    organism_count: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    ph_regm: Optional[str] = None
    perturbation: Optional[str] = None
    pesticide_regm: Optional[str] = None
    plant_growth_med: Optional[str] = None
    plant_product: Optional[str] = None
    plant_sex: Optional[str] = None
    plant_struc: Optional[str] = None
    radiation_regm: Optional[str] = None
    rainfall_regm: Optional[str] = None
    root_cond: Optional[str] = None
    root_med_carbon: Optional[str] = None
    root_med_macronutr: Optional[str] = None
    root_med_micronutr: Optional[str] = None
    root_med_suppl: Optional[str] = None
    root_med_ph: Optional[str] = None
    root_med_regl: Optional[str] = None
    root_med_solid: Optional[str] = None
    salt_regm: Optional[str] = None
    samp_capt_status: Optional[str] = None
    samp_dis_stage: Optional[str] = None
    samp_salinity: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    season_environment: Optional[str] = None
    standing_water_regm: Optional[str] = None
    temp: Optional[str] = None
    tiss_cult_growth_med: Optional[str] = None
    water_temp_regm: Optional[str] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.ances_data is not None and not isinstance(self.ances_data, str):
            self.ances_data = str(self.ances_data)

        if self.antibiotic_regm is not None and not isinstance(self.antibiotic_regm, str):
            self.antibiotic_regm = str(self.antibiotic_regm)

        if self.biol_stat is not None and not isinstance(self.biol_stat, str):
            self.biol_stat = str(self.biol_stat)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chem_mutagen is not None and not isinstance(self.chem_mutagen, str):
            self.chem_mutagen = str(self.chem_mutagen)

        if self.climate_environment is not None and not isinstance(self.climate_environment, str):
            self.climate_environment = str(self.climate_environment)

        if self.cult_root_med is not None and not isinstance(self.cult_root_med, str):
            self.cult_root_med = str(self.cult_root_med)

        if self.fertilizer_regm is not None and not isinstance(self.fertilizer_regm, str):
            self.fertilizer_regm = str(self.fertilizer_regm)

        if self.fungicide_regm is not None and not isinstance(self.fungicide_regm, str):
            self.fungicide_regm = str(self.fungicide_regm)

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.gravity is not None and not isinstance(self.gravity, str):
            self.gravity = str(self.gravity)

        if self.growth_facil is not None and not isinstance(self.growth_facil, str):
            self.growth_facil = str(self.growth_facil)

        if self.growth_habit is not None and not isinstance(self.growth_habit, str):
            self.growth_habit = str(self.growth_habit)

        if self.growth_hormone_regm is not None and not isinstance(self.growth_hormone_regm, str):
            self.growth_hormone_regm = str(self.growth_hormone_regm)

        if self.herbicide_regm is not None and not isinstance(self.herbicide_regm, str):
            self.herbicide_regm = str(self.herbicide_regm)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_common_name is not None and not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self.host_disease_stat is not None and not isinstance(self.host_disease_stat, str):
            self.host_disease_stat = str(self.host_disease_stat)

        if self.host_dry_mass is not None and not isinstance(self.host_dry_mass, str):
            self.host_dry_mass = str(self.host_dry_mass)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_infra_specific_name is not None and not isinstance(self.host_infra_specific_name, str):
            self.host_infra_specific_name = str(self.host_infra_specific_name)

        if self.host_infra_specific_rank is not None and not isinstance(self.host_infra_specific_rank, str):
            self.host_infra_specific_rank = str(self.host_infra_specific_rank)

        if self.host_length is not None and not isinstance(self.host_length, str):
            self.host_length = str(self.host_length)

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, str):
            self.host_life_stage = str(self.host_life_stage)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if self.host_taxid is not None and not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_wet_mass is not None and not isinstance(self.host_wet_mass, str):
            self.host_wet_mass = str(self.host_wet_mass)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.mechanical_damage is not None and not isinstance(self.mechanical_damage, str):
            self.mechanical_damage = str(self.mechanical_damage)

        if self.mineral_nutr_regm is not None and not isinstance(self.mineral_nutr_regm, str):
            self.mineral_nutr_regm = str(self.mineral_nutr_regm)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.non_mineral_nutr_regm is not None and not isinstance(self.non_mineral_nutr_regm, str):
            self.non_mineral_nutr_regm = str(self.non_mineral_nutr_regm)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.ph_regm is not None and not isinstance(self.ph_regm, str):
            self.ph_regm = str(self.ph_regm)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.pesticide_regm is not None and not isinstance(self.pesticide_regm, str):
            self.pesticide_regm = str(self.pesticide_regm)

        if self.plant_growth_med is not None and not isinstance(self.plant_growth_med, str):
            self.plant_growth_med = str(self.plant_growth_med)

        if self.plant_product is not None and not isinstance(self.plant_product, str):
            self.plant_product = str(self.plant_product)

        if self.plant_sex is not None and not isinstance(self.plant_sex, str):
            self.plant_sex = str(self.plant_sex)

        if self.plant_struc is not None and not isinstance(self.plant_struc, str):
            self.plant_struc = str(self.plant_struc)

        if self.radiation_regm is not None and not isinstance(self.radiation_regm, str):
            self.radiation_regm = str(self.radiation_regm)

        if self.rainfall_regm is not None and not isinstance(self.rainfall_regm, str):
            self.rainfall_regm = str(self.rainfall_regm)

        if self.root_cond is not None and not isinstance(self.root_cond, str):
            self.root_cond = str(self.root_cond)

        if self.root_med_carbon is not None and not isinstance(self.root_med_carbon, str):
            self.root_med_carbon = str(self.root_med_carbon)

        if self.root_med_macronutr is not None and not isinstance(self.root_med_macronutr, str):
            self.root_med_macronutr = str(self.root_med_macronutr)

        if self.root_med_micronutr is not None and not isinstance(self.root_med_micronutr, str):
            self.root_med_micronutr = str(self.root_med_micronutr)

        if self.root_med_suppl is not None and not isinstance(self.root_med_suppl, str):
            self.root_med_suppl = str(self.root_med_suppl)

        if self.root_med_ph is not None and not isinstance(self.root_med_ph, str):
            self.root_med_ph = str(self.root_med_ph)

        if self.root_med_regl is not None and not isinstance(self.root_med_regl, str):
            self.root_med_regl = str(self.root_med_regl)

        if self.root_med_solid is not None and not isinstance(self.root_med_solid, str):
            self.root_med_solid = str(self.root_med_solid)

        if self.salt_regm is not None and not isinstance(self.salt_regm, str):
            self.salt_regm = str(self.salt_regm)

        if self.samp_capt_status is not None and not isinstance(self.samp_capt_status, str):
            self.samp_capt_status = str(self.samp_capt_status)

        if self.samp_dis_stage is not None and not isinstance(self.samp_dis_stage, str):
            self.samp_dis_stage = str(self.samp_dis_stage)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.season_environment is not None and not isinstance(self.season_environment, str):
            self.season_environment = str(self.season_environment)

        if self.standing_water_regm is not None and not isinstance(self.standing_water_regm, str):
            self.standing_water_regm = str(self.standing_water_regm)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tiss_cult_growth_med is not None and not isinstance(self.tiss_cult_growth_med, str):
            self.tiss_cult_growth_med = str(self.tiss_cult_growth_med)

        if self.water_temp_regm is not None and not isinstance(self.water_temp_regm, str):
            self.water_temp_regm = str(self.water_temp_regm)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass
class Sediment(YAMLRoot):
    """
    sediment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB.Sediment
    class_class_curie: ClassVar[str] = "mixs.vocab:Sediment"
    class_name: ClassVar[str] = "sediment"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Sediment

    alkalinity: Optional[str] = None
    alkyl_diethers: Optional[str] = None
    aminopept_act: Optional[str] = None
    ammonium: Optional[str] = None
    bacteria_carb_prod: Optional[str] = None
    biomass: Optional[str] = None
    bishomohopanol: Optional[str] = None
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[str] = None
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    density: Optional[str] = None
    diether_lipids: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    glucosidase_act: Optional[str] = None
    magnesium: Optional[str] = None
    mean_frict_vel: Optional[str] = None
    mean_peak_frict_vel: Optional[str] = None
    methane: Optional[str] = None
    misc_param: Optional[str] = None
    n_alkanes: Optional[str] = None
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    organism_count: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    ph: Optional[str] = None
    particle_class: Optional[str] = None
    part_org_carb: Optional[str] = None
    perturbation: Optional[str] = None
    petroleum_hydrocarb: Optional[str] = None
    phaeopigments: Optional[str] = None
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[str] = None
    porosity: Optional[str] = None
    potassium: Optional[str] = None
    pressure: Optional[str] = None
    redox_potential: Optional[str] = None
    salinity: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    sediment_type: Optional[str] = None
    silicate: Optional[str] = None
    sodium: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    temp: Optional[str] = None
    tidal_stage: Optional[str] = None
    tot_carb: Optional[str] = None
    tot_depth_water_col: Optional[str] = None
    tot_nitro_content: Optional[str] = None
    tot_org_carb: Optional[str] = None
    turbidity: Optional[str] = None
    water_content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if self.biomass is not None and not isinstance(self.biomass, str):
            self.biomass = str(self.biomass)

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.diether_lipids is not None and not isinstance(self.diether_lipids, str):
            self.diether_lipids = str(self.diether_lipids)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.n_alkanes is not None and not isinstance(self.n_alkanes, str):
            self.n_alkanes = str(self.n_alkanes)

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.particle_class is not None and not isinstance(self.particle_class, str):
            self.particle_class = str(self.particle_class)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.phaeopigments is not None and not isinstance(self.phaeopigments, str):
            self.phaeopigments = str(self.phaeopigments)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.phosplipid_fatt_acid is not None and not isinstance(self.phosplipid_fatt_acid, str):
            self.phosplipid_fatt_acid = str(self.phosplipid_fatt_acid)

        if self.porosity is not None and not isinstance(self.porosity, str):
            self.porosity = str(self.porosity)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.sediment_type is not None and not isinstance(self.sediment_type, str):
            self.sediment_type = str(self.sediment_type)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, str):
            self.tidal_stage = str(self.tidal_stage)

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, str):
            self.tot_depth_water_col = str(self.tot_depth_water_col)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        super().__post_init__(**kwargs)


@dataclass
class Soil(YAMLRoot):
    """
    soil
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB.Soil
    class_class_curie: ClassVar[str] = "mixs.vocab:Soil"
    class_name: ClassVar[str] = "soil"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Soil

    cur_land_use: Optional[str] = None
    cur_vegetation: Optional[str] = None
    cur_vegetation_meth: Optional[str] = None
    previous_land_use: Optional[str] = None
    previous_land_use_meth: Optional[str] = None
    crop_rotation: Optional[str] = None
    agrochem_addition: Optional[str] = None
    tillage: Optional[str] = None
    fire: Optional[str] = None
    flooding: Optional[str] = None
    extreme_event: Optional[str] = None
    horizon: Optional[str] = None
    horizon_meth: Optional[str] = None
    sieving: Optional[str] = None
    water_content: Optional[str] = None
    water_content_soil_meth: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    pool_dna_extracts: Optional[str] = None
    store_cond: Optional[str] = None
    link_climate_info: Optional[str] = None
    annual_temp: Optional[str] = None
    season_temp: Optional[str] = None
    annual_precpt: Optional[str] = None
    season_precpt: Optional[str] = None
    link_class_info: Optional[str] = None
    fao_class: Optional[str] = None
    local_class: Optional[str] = None
    local_class_meth: Optional[str] = None
    soil_type: Optional[str] = None
    soil_type_meth: Optional[str] = None
    slope_gradient: Optional[str] = None
    slope_aspect: Optional[str] = None
    profile_position: Optional[str] = None
    drainage_class: Optional[str] = None
    texture: Optional[str] = None
    texture_meth: Optional[str] = None
    ph: Optional[str] = None
    ph_meth: Optional[str] = None
    tot_org_carb: Optional[str] = None
    tot_org_c_meth: Optional[str] = None
    tot_nitro_content: Optional[str] = None
    tot_nitro_content_meth: Optional[str] = None
    microbial_biomass: Optional[str] = None
    microbial_biomass_meth: Optional[str] = None
    link_addit_analys: Optional[str] = None
    extreme_salinity: Optional[str] = None
    salinity_meth: Optional[str] = None
    heavy_metals: Optional[str] = None
    heavy_metals_meth: Optional[str] = None
    al_sat: Optional[str] = None
    al_sat_meth: Optional[str] = None
    misc_param: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.cur_land_use is not None and not isinstance(self.cur_land_use, str):
            self.cur_land_use = str(self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, str):
            self.cur_vegetation = str(self.cur_vegetation)

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, str):
            self.cur_vegetation_meth = str(self.cur_vegetation_meth)

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, str):
            self.previous_land_use = str(self.previous_land_use)

        if self.previous_land_use_meth is not None and not isinstance(self.previous_land_use_meth, str):
            self.previous_land_use_meth = str(self.previous_land_use_meth)

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, str):
            self.crop_rotation = str(self.crop_rotation)

        if self.agrochem_addition is not None and not isinstance(self.agrochem_addition, str):
            self.agrochem_addition = str(self.agrochem_addition)

        if self.tillage is not None and not isinstance(self.tillage, str):
            self.tillage = str(self.tillage)

        if self.fire is not None and not isinstance(self.fire, str):
            self.fire = str(self.fire)

        if self.flooding is not None and not isinstance(self.flooding, str):
            self.flooding = str(self.flooding)

        if self.extreme_event is not None and not isinstance(self.extreme_event, str):
            self.extreme_event = str(self.extreme_event)

        if self.horizon is not None and not isinstance(self.horizon, str):
            self.horizon = str(self.horizon)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.sieving is not None and not isinstance(self.sieving, str):
            self.sieving = str(self.sieving)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if self.water_content_soil_meth is not None and not isinstance(self.water_content_soil_meth, str):
            self.water_content_soil_meth = str(self.water_content_soil_meth)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.pool_dna_extracts is not None and not isinstance(self.pool_dna_extracts, str):
            self.pool_dna_extracts = str(self.pool_dna_extracts)

        if self.store_cond is not None and not isinstance(self.store_cond, str):
            self.store_cond = str(self.store_cond)

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, str):
            self.link_climate_info = str(self.link_climate_info)

        if self.annual_temp is not None and not isinstance(self.annual_temp, str):
            self.annual_temp = str(self.annual_temp)

        if self.season_temp is not None and not isinstance(self.season_temp, str):
            self.season_temp = str(self.season_temp)

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, str):
            self.annual_precpt = str(self.annual_precpt)

        if self.season_precpt is not None and not isinstance(self.season_precpt, str):
            self.season_precpt = str(self.season_precpt)

        if self.link_class_info is not None and not isinstance(self.link_class_info, str):
            self.link_class_info = str(self.link_class_info)

        if self.fao_class is not None and not isinstance(self.fao_class, str):
            self.fao_class = str(self.fao_class)

        if self.local_class is not None and not isinstance(self.local_class, str):
            self.local_class = str(self.local_class)

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, str):
            self.local_class_meth = str(self.local_class_meth)

        if self.soil_type is not None and not isinstance(self.soil_type, str):
            self.soil_type = str(self.soil_type)

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, str):
            self.soil_type_meth = str(self.soil_type_meth)

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, str):
            self.slope_gradient = str(self.slope_gradient)

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, str):
            self.slope_aspect = str(self.slope_aspect)

        if self.profile_position is not None and not isinstance(self.profile_position, str):
            self.profile_position = str(self.profile_position)

        if self.drainage_class is not None and not isinstance(self.drainage_class, str):
            self.drainage_class = str(self.drainage_class)

        if self.texture is not None and not isinstance(self.texture, str):
            self.texture = str(self.texture)

        if self.texture_meth is not None and not isinstance(self.texture_meth, str):
            self.texture_meth = str(self.texture_meth)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, str):
            self.tot_org_c_meth = str(self.tot_org_c_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_nitro_content_meth is not None and not isinstance(self.tot_nitro_content_meth, str):
            self.tot_nitro_content_meth = str(self.tot_nitro_content_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, str):
            self.microbial_biomass = str(self.microbial_biomass)

        if self.microbial_biomass_meth is not None and not isinstance(self.microbial_biomass_meth, str):
            self.microbial_biomass_meth = str(self.microbial_biomass_meth)

        if self.link_addit_analys is not None and not isinstance(self.link_addit_analys, str):
            self.link_addit_analys = str(self.link_addit_analys)

        if self.extreme_salinity is not None and not isinstance(self.extreme_salinity, str):
            self.extreme_salinity = str(self.extreme_salinity)

        if self.salinity_meth is not None and not isinstance(self.salinity_meth, str):
            self.salinity_meth = str(self.salinity_meth)

        if self.heavy_metals is not None and not isinstance(self.heavy_metals, str):
            self.heavy_metals = str(self.heavy_metals)

        if self.heavy_metals_meth is not None and not isinstance(self.heavy_metals_meth, str):
            self.heavy_metals_meth = str(self.heavy_metals_meth)

        if self.al_sat is not None and not isinstance(self.al_sat, str):
            self.al_sat = str(self.al_sat)

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, str):
            self.al_sat_meth = str(self.al_sat_meth)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        super().__post_init__(**kwargs)


@dataclass
class WastewaterSludge(YAMLRoot):
    """
    wastewater/sludge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB.WastewaterSludge
    class_class_curie: ClassVar[str] = "mixs.vocab:WastewaterSludge"
    class_name: ClassVar[str] = "wastewater_sludge"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.WastewaterSludge

    alkalinity: Optional[str] = None
    biochem_oxygen_dem: Optional[str] = None
    chem_administration: Optional[str] = None
    chem_oxygen_dem: Optional[str] = None
    efficiency_percent: Optional[str] = None
    emulsions: Optional[str] = None
    gaseous_substances: Optional[str] = None
    indust_eff_percent: Optional[str] = None
    inorg_particles: Optional[str] = None
    misc_param: Optional[str] = None
    nitrate: Optional[str] = None
    org_particles: Optional[str] = None
    organism_count: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    ph: Optional[str] = None
    perturbation: Optional[str] = None
    phosphate: Optional[str] = None
    pre_treatment: Optional[str] = None
    primary_treatment: Optional[str] = None
    reactor_type: Optional[str] = None
    samp_salinity: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    secondary_treatment: Optional[str] = None
    sewage_type: Optional[str] = None
    sludge_retent_time: Optional[str] = None
    sodium: Optional[str] = None
    soluble_inorg_mat: Optional[str] = None
    soluble_org_mat: Optional[str] = None
    suspend_solids: Optional[str] = None
    temp: Optional[str] = None
    tertiary_treatment: Optional[str] = None
    tot_nitro: Optional[str] = None
    tot_phosphate: Optional[str] = None
    wastewater_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.biochem_oxygen_dem is not None and not isinstance(self.biochem_oxygen_dem, str):
            self.biochem_oxygen_dem = str(self.biochem_oxygen_dem)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chem_oxygen_dem is not None and not isinstance(self.chem_oxygen_dem, str):
            self.chem_oxygen_dem = str(self.chem_oxygen_dem)

        if self.efficiency_percent is not None and not isinstance(self.efficiency_percent, str):
            self.efficiency_percent = str(self.efficiency_percent)

        if self.emulsions is not None and not isinstance(self.emulsions, str):
            self.emulsions = str(self.emulsions)

        if self.gaseous_substances is not None and not isinstance(self.gaseous_substances, str):
            self.gaseous_substances = str(self.gaseous_substances)

        if self.indust_eff_percent is not None and not isinstance(self.indust_eff_percent, str):
            self.indust_eff_percent = str(self.indust_eff_percent)

        if self.inorg_particles is not None and not isinstance(self.inorg_particles, str):
            self.inorg_particles = str(self.inorg_particles)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.org_particles is not None and not isinstance(self.org_particles, str):
            self.org_particles = str(self.org_particles)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.pre_treatment is not None and not isinstance(self.pre_treatment, str):
            self.pre_treatment = str(self.pre_treatment)

        if self.primary_treatment is not None and not isinstance(self.primary_treatment, str):
            self.primary_treatment = str(self.primary_treatment)

        if self.reactor_type is not None and not isinstance(self.reactor_type, str):
            self.reactor_type = str(self.reactor_type)

        if self.samp_salinity is not None and not isinstance(self.samp_salinity, str):
            self.samp_salinity = str(self.samp_salinity)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.secondary_treatment is not None and not isinstance(self.secondary_treatment, str):
            self.secondary_treatment = str(self.secondary_treatment)

        if self.sewage_type is not None and not isinstance(self.sewage_type, str):
            self.sewage_type = str(self.sewage_type)

        if self.sludge_retent_time is not None and not isinstance(self.sludge_retent_time, str):
            self.sludge_retent_time = str(self.sludge_retent_time)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.soluble_inorg_mat is not None and not isinstance(self.soluble_inorg_mat, str):
            self.soluble_inorg_mat = str(self.soluble_inorg_mat)

        if self.soluble_org_mat is not None and not isinstance(self.soluble_org_mat, str):
            self.soluble_org_mat = str(self.soluble_org_mat)

        if self.suspend_solids is not None and not isinstance(self.suspend_solids, str):
            self.suspend_solids = str(self.suspend_solids)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tertiary_treatment is not None and not isinstance(self.tertiary_treatment, str):
            self.tertiary_treatment = str(self.tertiary_treatment)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_phosphate is not None and not isinstance(self.tot_phosphate, str):
            self.tot_phosphate = str(self.tot_phosphate)

        if self.wastewater_type is not None and not isinstance(self.wastewater_type, str):
            self.wastewater_type = str(self.wastewater_type)

        super().__post_init__(**kwargs)


@dataclass
class Water(YAMLRoot):
    """
    water
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.VOCAB.Water
    class_class_curie: ClassVar[str] = "mixs.vocab:Water"
    class_name: ClassVar[str] = "water"
    class_model_uri: ClassVar[URIRef] = MIXS.VOCAB.Water

    alkalinity: Optional[str] = None
    alkalinity_method: Optional[str] = None
    alkyl_diethers: Optional[str] = None
    aminopept_act: Optional[str] = None
    ammonium: Optional[str] = None
    atmospheric_data: Optional[str] = None
    bacteria_carb_prod: Optional[str] = None
    bac_prod: Optional[str] = None
    bac_resp: Optional[str] = None
    biomass: Optional[str] = None
    bishomohopanol: Optional[str] = None
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[str] = None
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    conduc: Optional[str] = None
    density: Optional[str] = None
    diether_lipids: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_inorg_nitro: Optional[str] = None
    diss_inorg_phosp: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    down_par: Optional[str] = None
    fluor: Optional[str] = None
    glucosidase_act: Optional[str] = None
    light_intensity: Optional[str] = None
    magnesium: Optional[str] = None
    mean_frict_vel: Optional[str] = None
    mean_peak_frict_vel: Optional[str] = None
    misc_param: Optional[str] = None
    n_alkanes: Optional[str] = None
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    organism_count: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    ph: Optional[str] = None
    part_org_carb: Optional[str] = None
    part_org_nitro: Optional[str] = None
    perturbation: Optional[str] = None
    petroleum_hydrocarb: Optional[str] = None
    phaeopigments: Optional[str] = None
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[str] = None
    photon_flux: Optional[str] = None
    potassium: Optional[str] = None
    pressure: Optional[str] = None
    primary_prod: Optional[str] = None
    redox_potential: Optional[str] = None
    salinity: Optional[str] = None
    samp_store_dur: Optional[str] = None
    samp_store_loc: Optional[str] = None
    samp_store_temp: Optional[str] = None
    samp_vol_we_dna_ext: Optional[str] = None
    silicate: Optional[str] = None
    size_frac_low: Optional[str] = None
    size_frac_up: Optional[str] = None
    sodium: Optional[str] = None
    soluble_react_phosp: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    suspend_part_matter: Optional[str] = None
    temp: Optional[str] = None
    tidal_stage: Optional[str] = None
    tot_depth_water_col: Optional[str] = None
    tot_diss_nitro: Optional[str] = None
    tot_inorg_nitro: Optional[str] = None
    tot_nitro: Optional[str] = None
    tot_part_carb: Optional[str] = None
    tot_phosp: Optional[str] = None
    turbidity: Optional[str] = None
    water_current: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.atmospheric_data is not None and not isinstance(self.atmospheric_data, str):
            self.atmospheric_data = str(self.atmospheric_data)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if self.bac_prod is not None and not isinstance(self.bac_prod, str):
            self.bac_prod = str(self.bac_prod)

        if self.bac_resp is not None and not isinstance(self.bac_resp, str):
            self.bac_resp = str(self.bac_resp)

        if self.biomass is not None and not isinstance(self.biomass, str):
            self.biomass = str(self.biomass)

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.conduc is not None and not isinstance(self.conduc, str):
            self.conduc = str(self.conduc)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.diether_lipids is not None and not isinstance(self.diether_lipids, str):
            self.diether_lipids = str(self.diether_lipids)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_nitro is not None and not isinstance(self.diss_inorg_nitro, str):
            self.diss_inorg_nitro = str(self.diss_inorg_nitro)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.down_par is not None and not isinstance(self.down_par, str):
            self.down_par = str(self.down_par)

        if self.fluor is not None and not isinstance(self.fluor, str):
            self.fluor = str(self.fluor)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.light_intensity is not None and not isinstance(self.light_intensity, str):
            self.light_intensity = str(self.light_intensity)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.n_alkanes is not None and not isinstance(self.n_alkanes, str):
            self.n_alkanes = str(self.n_alkanes)

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if self.part_org_nitro is not None and not isinstance(self.part_org_nitro, str):
            self.part_org_nitro = str(self.part_org_nitro)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.phaeopigments is not None and not isinstance(self.phaeopigments, str):
            self.phaeopigments = str(self.phaeopigments)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.phosplipid_fatt_acid is not None and not isinstance(self.phosplipid_fatt_acid, str):
            self.phosplipid_fatt_acid = str(self.phosplipid_fatt_acid)

        if self.photon_flux is not None and not isinstance(self.photon_flux, str):
            self.photon_flux = str(self.photon_flux)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.primary_prod is not None and not isinstance(self.primary_prod, str):
            self.primary_prod = str(self.primary_prod)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.samp_store_dur is not None and not isinstance(self.samp_store_dur, str):
            self.samp_store_dur = str(self.samp_store_dur)

        if self.samp_store_loc is not None and not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, str):
            self.samp_store_temp = str(self.samp_store_temp)

        if self.samp_vol_we_dna_ext is not None and not isinstance(self.samp_vol_we_dna_ext, str):
            self.samp_vol_we_dna_ext = str(self.samp_vol_we_dna_ext)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.soluble_react_phosp is not None and not isinstance(self.soluble_react_phosp, str):
            self.soluble_react_phosp = str(self.soluble_react_phosp)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.suspend_part_matter is not None and not isinstance(self.suspend_part_matter, str):
            self.suspend_part_matter = str(self.suspend_part_matter)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, str):
            self.tidal_stage = str(self.tidal_stage)

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, str):
            self.tot_depth_water_col = str(self.tot_depth_water_col)

        if self.tot_diss_nitro is not None and not isinstance(self.tot_diss_nitro, str):
            self.tot_diss_nitro = str(self.tot_diss_nitro)

        if self.tot_inorg_nitro is not None and not isinstance(self.tot_inorg_nitro, str):
            self.tot_inorg_nitro = str(self.tot_inorg_nitro)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_part_carb is not None and not isinstance(self.tot_part_carb, str):
            self.tot_part_carb = str(self.tot_part_carb)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if self.water_current is not None and not isinstance(self.water_current, str):
            self.water_current = str(self.water_current)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.core_field = Slot(uri=MIXS.VOCAB.core_field, name="core field", curie=MIXS.VOCAB.curie('core_field'),
                   model_uri=MIXS.VOCAB.core_field, domain=None, range=Optional[str])

slots.investigation_field = Slot(uri=MIXS.VOCAB.investigation_field, name="investigation field", curie=MIXS.VOCAB.curie('investigation_field'),
                   model_uri=MIXS.VOCAB.investigation_field, domain=None, range=Optional[str])

slots.nucleic_acid_sequence_source_field = Slot(uri=MIXS.VOCAB.nucleic_acid_sequence_source_field, name="nucleic acid sequence source field", curie=MIXS.VOCAB.curie('nucleic_acid_sequence_source_field'),
                   model_uri=MIXS.VOCAB.nucleic_acid_sequence_source_field, domain=None, range=Optional[str])

slots.sequencing_field = Slot(uri=MIXS.VOCAB.sequencing_field, name="sequencing field", curie=MIXS.VOCAB.curie('sequencing_field'),
                   model_uri=MIXS.VOCAB.sequencing_field, domain=None, range=Optional[str])

slots.mixs_extension_field = Slot(uri=MIXS.VOCAB.mixs_extension_field, name="mixs extension field", curie=MIXS.VOCAB.curie('mixs_extension_field'),
                   model_uri=MIXS.VOCAB.mixs_extension_field, domain=None, range=Optional[str])

slots.environment_field = Slot(uri=MIXS.VOCAB.environment_field, name="environment field", curie=MIXS.VOCAB.curie('environment_field'),
                   model_uri=MIXS.VOCAB.environment_field, domain=None, range=Optional[str])

slots.submitted_to_insdc = Slot(uri=MIXS.VOCAB.submitted_to_insdc, name="submitted_to_insdc", curie=MIXS.VOCAB.curie('submitted_to_insdc'),
                   model_uri=MIXS.VOCAB.submitted_to_insdc, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean}'))

slots.investigation_type = Slot(uri=MIXS.VOCAB.investigation_type, name="investigation_type", curie=MIXS.VOCAB.curie('investigation_type'),
                   model_uri=MIXS.VOCAB.investigation_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[eukaryote|bacteria_archaea|plasmid|virus|organelle|metagenome|metatranscriptome|mimarks-survey|mimarks-specimen|misag|mimag|miuvig]'))

slots.sample_name = Slot(uri=MIXS.VOCAB.sample_name, name="sample_name", curie=MIXS.VOCAB.curie('sample_name'),
                   model_uri=MIXS.VOCAB.sample_name, domain=None, range=Optional[str])

slots.project_name = Slot(uri=MIXS.VOCAB.project_name, name="project_name", curie=MIXS.VOCAB.curie('project_name'),
                   model_uri=MIXS.VOCAB.project_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.experimental_factor = Slot(uri=MIXS.VOCAB.experimental_factor, name="experimental_factor", curie=MIXS.VOCAB.curie('experimental_factor'),
                   model_uri=MIXS.VOCAB.experimental_factor, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}|{text}'))

slots.lat_lon = Slot(uri=MIXS.VOCAB.lat_lon, name="lat_lon", curie=MIXS.VOCAB.curie('lat_lon'),
                   model_uri=MIXS.VOCAB.lat_lon, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {float}'))

slots.depth = Slot(uri=MIXS.VOCAB.depth, name="depth", curie=MIXS.VOCAB.curie('depth'),
                   model_uri=MIXS.VOCAB.depth, domain=None, range=Optional[str],
                   pattern=re.compile(r'-'))

slots.alt = Slot(uri=MIXS.VOCAB.alt, name="alt", curie=MIXS.VOCAB.curie('alt'),
                   model_uri=MIXS.VOCAB.alt, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.elev = Slot(uri=MIXS.VOCAB.elev, name="elev", curie=MIXS.VOCAB.curie('elev'),
                   model_uri=MIXS.VOCAB.elev, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.geo_loc_name = Slot(uri=MIXS.VOCAB.geo_loc_name, name="geo_loc_name", curie=MIXS.VOCAB.curie('geo_loc_name'),
                   model_uri=MIXS.VOCAB.geo_loc_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'{term};{term};{text}'))

slots.collection_date = Slot(uri=MIXS.VOCAB.collection_date, name="collection_date", curie=MIXS.VOCAB.curie('collection_date'),
                   model_uri=MIXS.VOCAB.collection_date, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.env_broad_scale = Slot(uri=MIXS.VOCAB.env_broad_scale, name="env_broad_scale", curie=MIXS.VOCAB.curie('env_broad_scale'),
                   model_uri=MIXS.VOCAB.env_broad_scale, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}'))

slots.env_local_scale = Slot(uri=MIXS.VOCAB.env_local_scale, name="env_local_scale", curie=MIXS.VOCAB.curie('env_local_scale'),
                   model_uri=MIXS.VOCAB.env_local_scale, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}'))

slots.env_medium = Slot(uri=MIXS.VOCAB.env_medium, name="env_medium", curie=MIXS.VOCAB.curie('env_medium'),
                   model_uri=MIXS.VOCAB.env_medium, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}'))

slots.env_package = Slot(uri=MIXS.VOCAB.env_package, name="env_package", curie=MIXS.VOCAB.curie('env_package'),
                   model_uri=MIXS.VOCAB.env_package, domain=None, range=Optional[str],
                   pattern=re.compile(r'[air|built environment|host-associated|human-associated|human-skin|human-oral|human-gut|human-vaginal|hydrocarbon resources-cores|hydrocarbon resources-fluids/swabs|microbial mat/biofilm|misc environment|plant-associated|sediment|soil|wastewater/sludge|water]'))

slots.subspecf_gen_lin = Slot(uri=MIXS.VOCAB.subspecf_gen_lin, name="subspecf_gen_lin", curie=MIXS.VOCAB.curie('subspecf_gen_lin'),
                   model_uri=MIXS.VOCAB.subspecf_gen_lin, domain=None, range=Optional[str],
                   pattern=re.compile(r'{rank name}:{text}'))

slots.ploidy = Slot(uri=MIXS.VOCAB.ploidy, name="ploidy", curie=MIXS.VOCAB.curie('ploidy'),
                   model_uri=MIXS.VOCAB.ploidy, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}'))

slots.num_replicons = Slot(uri=MIXS.VOCAB.num_replicons, name="num_replicons", curie=MIXS.VOCAB.curie('num_replicons'),
                   model_uri=MIXS.VOCAB.num_replicons, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.extrachrom_elements = Slot(uri=MIXS.VOCAB.extrachrom_elements, name="extrachrom_elements", curie=MIXS.VOCAB.curie('extrachrom_elements'),
                   model_uri=MIXS.VOCAB.extrachrom_elements, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.estimated_size = Slot(uri=MIXS.VOCAB.estimated_size, name="estimated_size", curie=MIXS.VOCAB.curie('estimated_size'),
                   model_uri=MIXS.VOCAB.estimated_size, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer} bp'))

slots.ref_biomaterial = Slot(uri=MIXS.VOCAB.ref_biomaterial, name="ref_biomaterial", curie=MIXS.VOCAB.curie('ref_biomaterial'),
                   model_uri=MIXS.VOCAB.ref_biomaterial, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.source_mat_id = Slot(uri=MIXS.VOCAB.source_mat_id, name="source_mat_id", curie=MIXS.VOCAB.curie('source_mat_id'),
                   model_uri=MIXS.VOCAB.source_mat_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.pathogenicity = Slot(uri=MIXS.VOCAB.pathogenicity, name="pathogenicity", curie=MIXS.VOCAB.curie('pathogenicity'),
                   model_uri=MIXS.VOCAB.pathogenicity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.biotic_relationship = Slot(uri=MIXS.VOCAB.biotic_relationship, name="biotic_relationship", curie=MIXS.VOCAB.curie('biotic_relationship'),
                   model_uri=MIXS.VOCAB.biotic_relationship, domain=None, range=Optional[str],
                   pattern=re.compile(r'[free living|parasitism|commensalism|symbiotic|mutualism]'))

slots.specific_host = Slot(uri=MIXS.VOCAB.specific_host, name="specific_host", curie=MIXS.VOCAB.curie('specific_host'),
                   model_uri=MIXS.VOCAB.specific_host, domain=None, range=Optional[str],
                   pattern=re.compile(r'{NCBI taxid}|{text}'))

slots.host_spec_range = Slot(uri=MIXS.VOCAB.host_spec_range, name="host_spec_range", curie=MIXS.VOCAB.curie('host_spec_range'),
                   model_uri=MIXS.VOCAB.host_spec_range, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.health_disease_stat = Slot(uri=MIXS.VOCAB.health_disease_stat, name="health_disease_stat", curie=MIXS.VOCAB.curie('health_disease_stat'),
                   model_uri=MIXS.VOCAB.health_disease_stat, domain=None, range=Optional[str],
                   pattern=re.compile(r'[healthy|diseased|dead|disease-free|undetermined|recovering|resolving|pre-existing condition|pathological|life threatening|congenital]'))

slots.trophic_level = Slot(uri=MIXS.VOCAB.trophic_level, name="trophic_level", curie=MIXS.VOCAB.curie('trophic_level'),
                   model_uri=MIXS.VOCAB.trophic_level, domain=None, range=Optional[str],
                   pattern=re.compile(r'[autotroph|carboxydotroph|chemoautotroph|chemoheterotroph|chemolithoautotroph|chemolithotroph|chemoorganoheterotroph|chemoorganotroph|chemosynthetic|chemotroph|copiotroph|diazotroph|facultative|autotroph|heterotroph|lithoautotroph|lithoheterotroph|lithotroph|methanotroph|methylotroph|mixotroph|obligate|chemoautolithotroph|oligotroph|organoheterotroph|organotroph|photoautotroph|photoheterotroph|photolithoautotroph|photolithotroph|photosynthetic|phototroph]'))

slots.propagation = Slot(uri=MIXS.VOCAB.propagation, name="propagation", curie=MIXS.VOCAB.curie('propagation'),
                   model_uri=MIXS.VOCAB.propagation, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.encoded_traits = Slot(uri=MIXS.VOCAB.encoded_traits, name="encoded_traits", curie=MIXS.VOCAB.curie('encoded_traits'),
                   model_uri=MIXS.VOCAB.encoded_traits, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.rel_to_oxygen = Slot(uri=MIXS.VOCAB.rel_to_oxygen, name="rel_to_oxygen", curie=MIXS.VOCAB.curie('rel_to_oxygen'),
                   model_uri=MIXS.VOCAB.rel_to_oxygen, domain=None, range=Optional[str],
                   pattern=re.compile(r'[aerobe|anaerobe|facultative|microaerophilic|microanaerobe|obligate aerobe|obligate anaerobe]'))

slots.isol_growth_condt = Slot(uri=MIXS.VOCAB.isol_growth_condt, name="isol_growth_condt", curie=MIXS.VOCAB.curie('isol_growth_condt'),
                   model_uri=MIXS.VOCAB.isol_growth_condt, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.samp_collect_device = Slot(uri=MIXS.VOCAB.samp_collect_device, name="samp_collect_device", curie=MIXS.VOCAB.curie('samp_collect_device'),
                   model_uri=MIXS.VOCAB.samp_collect_device, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.samp_mat_process = Slot(uri=MIXS.VOCAB.samp_mat_process, name="samp_mat_process", curie=MIXS.VOCAB.curie('samp_mat_process'),
                   model_uri=MIXS.VOCAB.samp_mat_process, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}|{termLabel} {[termID]}'))

slots.size_frac = Slot(uri=MIXS.VOCAB.size_frac, name="size_frac", curie=MIXS.VOCAB.curie('size_frac'),
                   model_uri=MIXS.VOCAB.size_frac, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float}-{float} {unit}'))

slots.samp_size = Slot(uri=MIXS.VOCAB.samp_size, name="samp_size", curie=MIXS.VOCAB.curie('samp_size'),
                   model_uri=MIXS.VOCAB.samp_size, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.source_uvig = Slot(uri=MIXS.VOCAB.source_uvig, name="source_uvig", curie=MIXS.VOCAB.curie('source_uvig'),
                   model_uri=MIXS.VOCAB.source_uvig, domain=None, range=Optional[str],
                   pattern=re.compile(r'[metagenome (not viral targeted)|viral fraction metagenome (virome)|sequence-targeted metagenome|metatranscriptome (not viral targeted)|viral fraction RNA metagenome (RNA virome)|sequence-targeted RNA metagenome|microbial single amplified genome (SAG)|viral single amplified genome (vSAG)|isolate microbial genome|other]'))

slots.virus_enrich_appr = Slot(uri=MIXS.VOCAB.virus_enrich_appr, name="virus_enrich_appr", curie=MIXS.VOCAB.curie('virus_enrich_appr'),
                   model_uri=MIXS.VOCAB.virus_enrich_appr, domain=None, range=Optional[str],
                   pattern=re.compile(r'[filtration|ultrafiltration|centrifugation|ultracentrifugation|PEG Precipitation|FeCl Precipitation|CsCl density gradient|DNAse|RNAse|targeted sequence capture|other|none]'))

slots.nucl_acid_ext = Slot(uri=MIXS.VOCAB.nucl_acid_ext, name="nucl_acid_ext", curie=MIXS.VOCAB.curie('nucl_acid_ext'),
                   model_uri=MIXS.VOCAB.nucl_acid_ext, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.nucl_acid_amp = Slot(uri=MIXS.VOCAB.nucl_acid_amp, name="nucl_acid_amp", curie=MIXS.VOCAB.curie('nucl_acid_amp'),
                   model_uri=MIXS.VOCAB.nucl_acid_amp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.lib_size = Slot(uri=MIXS.VOCAB.lib_size, name="lib_size", curie=MIXS.VOCAB.curie('lib_size'),
                   model_uri=MIXS.VOCAB.lib_size, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.lib_reads_seqd = Slot(uri=MIXS.VOCAB.lib_reads_seqd, name="lib_reads_seqd", curie=MIXS.VOCAB.curie('lib_reads_seqd'),
                   model_uri=MIXS.VOCAB.lib_reads_seqd, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.lib_layout = Slot(uri=MIXS.VOCAB.lib_layout, name="lib_layout", curie=MIXS.VOCAB.curie('lib_layout'),
                   model_uri=MIXS.VOCAB.lib_layout, domain=None, range=Optional[str],
                   pattern=re.compile(r'[paired|single|vector|other]'))

slots.lib_vector = Slot(uri=MIXS.VOCAB.lib_vector, name="lib_vector", curie=MIXS.VOCAB.curie('lib_vector'),
                   model_uri=MIXS.VOCAB.lib_vector, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.lib_screen = Slot(uri=MIXS.VOCAB.lib_screen, name="lib_screen", curie=MIXS.VOCAB.curie('lib_screen'),
                   model_uri=MIXS.VOCAB.lib_screen, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.target_gene = Slot(uri=MIXS.VOCAB.target_gene, name="target_gene", curie=MIXS.VOCAB.curie('target_gene'),
                   model_uri=MIXS.VOCAB.target_gene, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.target_subfragment = Slot(uri=MIXS.VOCAB.target_subfragment, name="target_subfragment", curie=MIXS.VOCAB.curie('target_subfragment'),
                   model_uri=MIXS.VOCAB.target_subfragment, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.pcr_primers = Slot(uri=MIXS.VOCAB.pcr_primers, name="pcr_primers", curie=MIXS.VOCAB.curie('pcr_primers'),
                   model_uri=MIXS.VOCAB.pcr_primers, domain=None, range=Optional[str],
                   pattern=re.compile(r'FWD:{dna};REV:{dna}'))

slots.mid = Slot(uri=MIXS.VOCAB.mid, name="mid", curie=MIXS.VOCAB.curie('mid'),
                   model_uri=MIXS.VOCAB.mid, domain=None, range=Optional[str],
                   pattern=re.compile(r'{dna}'))

slots.adapters = Slot(uri=MIXS.VOCAB.adapters, name="adapters", curie=MIXS.VOCAB.curie('adapters'),
                   model_uri=MIXS.VOCAB.adapters, domain=None, range=Optional[str],
                   pattern=re.compile(r'{dna};{dna}'))

slots.pcr_cond = Slot(uri=MIXS.VOCAB.pcr_cond, name="pcr_cond", curie=MIXS.VOCAB.curie('pcr_cond'),
                   model_uri=MIXS.VOCAB.pcr_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'initial denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final elongation:degrees_minutes;total cycles'))

slots.seq_meth = Slot(uri=MIXS.VOCAB.seq_meth, name="seq_meth", curie=MIXS.VOCAB.curie('seq_meth'),
                   model_uri=MIXS.VOCAB.seq_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'[454 GS|454 GS 20|454 GS FLX|454 GS FLX+|454 GS FLX Titanium|454 GS Junior|AB 310 Genetic Analyzer|AB 3130 Genetic Analyzer|AB 3130xL Genetic Analyzer|AB 3500 Genetic Analyzer|AB 3500xL Genetic Analyzer|AB 3730 Genetic Analyzer|AB 3730xL Genetic Analyzer|AB 5500 Genetic Analyzer|AB 5500xl Genetic Analyzer|AB 5500xl-W Genetic Analysis System|AB SOLiD System|AB SOLiD System 2.0|AB SOLiD System 3.0|AB SOLiD 3 Plus System|AB SOLiD 4 System|AB SOLiD 4hq System|AB SOLiD PI System|BGISEQ-500|GridION|Illumina Genome Analyzer|Illumina Genome Analyzer II|Illumina Genome Analyzer IIx|Illumina HiSeq 1000|Illumina HiSeq 1500|Illumina HiSeq 2000|Illumina HiSeq 2500|Illumina HiSeq 3000|Illumina HiSeq 4000|Illumina HiScanSQ|Illumina MiSeq|Illumina HiSeq X Five|Illumina HiSeq X Ten|Illumina NextSeq 500|Illumina NextSeq 550|Ion Torrent PGM|Ion Torrent Proton|Ion Torrent S5|Ion Torrent S5 XL|MinION|PacBio RS|PacBio RS II|PromethION|Sequel]'))

slots.seq_quality_check = Slot(uri=MIXS.VOCAB.seq_quality_check, name="seq_quality_check", curie=MIXS.VOCAB.curie('seq_quality_check'),
                   model_uri=MIXS.VOCAB.seq_quality_check, domain=None, range=Optional[str],
                   pattern=re.compile(r'[none|manually edited]'))

slots.chimera_check = Slot(uri=MIXS.VOCAB.chimera_check, name="chimera_check", curie=MIXS.VOCAB.curie('chimera_check'),
                   model_uri=MIXS.VOCAB.chimera_check, domain=None, range=Optional[str],
                   pattern=re.compile(r'{software};{version};{parameters}'))

slots.tax_ident = Slot(uri=MIXS.VOCAB.tax_ident, name="tax_ident", curie=MIXS.VOCAB.curie('tax_ident'),
                   model_uri=MIXS.VOCAB.tax_ident, domain=None, range=Optional[str],
                   pattern=re.compile(r'[16S rRNA gene|multi-marker approach|other]'))

slots.assembly_qual = Slot(uri=MIXS.VOCAB.assembly_qual, name="assembly_qual", curie=MIXS.VOCAB.curie('assembly_qual'),
                   model_uri=MIXS.VOCAB.assembly_qual, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Finished genome|High-quality draft genome|Medium-quality draft genome|Low-quality draft genome|Genome fragment(s)]'))

slots.assembly_name = Slot(uri=MIXS.VOCAB.assembly_name, name="assembly_name", curie=MIXS.VOCAB.curie('assembly_name'),
                   model_uri=MIXS.VOCAB.assembly_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text} {text}'))

slots.assembly_software = Slot(uri=MIXS.VOCAB.assembly_software, name="assembly_software", curie=MIXS.VOCAB.curie('assembly_software'),
                   model_uri=MIXS.VOCAB.assembly_software, domain=None, range=Optional[str],
                   pattern=re.compile(r'{software};{version};{parameters}'))

slots.annot = Slot(uri=MIXS.VOCAB.annot, name="annot", curie=MIXS.VOCAB.curie('annot'),
                   model_uri=MIXS.VOCAB.annot, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.number_contig = Slot(uri=MIXS.VOCAB.number_contig, name="number_contig", curie=MIXS.VOCAB.curie('number_contig'),
                   model_uri=MIXS.VOCAB.number_contig, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.feat_pred = Slot(uri=MIXS.VOCAB.feat_pred, name="feat_pred", curie=MIXS.VOCAB.curie('feat_pred'),
                   model_uri=MIXS.VOCAB.feat_pred, domain=None, range=Optional[str],
                   pattern=re.compile(r'{software};{version};{parameters}'))

slots.ref_db = Slot(uri=MIXS.VOCAB.ref_db, name="ref_db", curie=MIXS.VOCAB.curie('ref_db'),
                   model_uri=MIXS.VOCAB.ref_db, domain=None, range=Optional[str],
                   pattern=re.compile(r'{database};{version};{reference}'))

slots.sim_search_meth = Slot(uri=MIXS.VOCAB.sim_search_meth, name="sim_search_meth", curie=MIXS.VOCAB.curie('sim_search_meth'),
                   model_uri=MIXS.VOCAB.sim_search_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{software};{version};{parameters}'))

slots.tax_class = Slot(uri=MIXS.VOCAB.tax_class, name="tax_class", curie=MIXS.VOCAB.curie('tax_class'),
                   model_uri=MIXS.VOCAB.tax_class, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.x_16s_recover = Slot(uri=MIXS.VOCAB.x_16s_recover, name="x_16s_recover", curie=MIXS.VOCAB.curie('x_16s_recover'),
                   model_uri=MIXS.VOCAB.x_16s_recover, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean}'))

slots.x_16s_recover_software = Slot(uri=MIXS.VOCAB.x_16s_recover_software, name="x_16s_recover_software", curie=MIXS.VOCAB.curie('x_16s_recover_software'),
                   model_uri=MIXS.VOCAB.x_16s_recover_software, domain=None, range=Optional[str],
                   pattern=re.compile(r'{software};{version};{parameters}'))

slots.trnas = Slot(uri=MIXS.VOCAB.trnas, name="trnas", curie=MIXS.VOCAB.curie('trnas'),
                   model_uri=MIXS.VOCAB.trnas, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.trna_ext_software = Slot(uri=MIXS.VOCAB.trna_ext_software, name="trna_ext_software", curie=MIXS.VOCAB.curie('trna_ext_software'),
                   model_uri=MIXS.VOCAB.trna_ext_software, domain=None, range=Optional[str],
                   pattern=re.compile(r'{software};{version};{parameters}'))

slots.compl_score = Slot(uri=MIXS.VOCAB.compl_score, name="compl_score", curie=MIXS.VOCAB.curie('compl_score'),
                   model_uri=MIXS.VOCAB.compl_score, domain=None, range=Optional[str],
                   pattern=re.compile(r'[high|med|low];{percentage}'))

slots.compl_software = Slot(uri=MIXS.VOCAB.compl_software, name="compl_software", curie=MIXS.VOCAB.curie('compl_software'),
                   model_uri=MIXS.VOCAB.compl_software, domain=None, range=Optional[str],
                   pattern=re.compile(r'{software};{version}'))

slots.compl_appr = Slot(uri=MIXS.VOCAB.compl_appr, name="compl_appr", curie=MIXS.VOCAB.curie('compl_appr'),
                   model_uri=MIXS.VOCAB.compl_appr, domain=None, range=Optional[str],
                   pattern=re.compile(r'[marker gene|reference based|other]'))

slots.contam_score = Slot(uri=MIXS.VOCAB.contam_score, name="contam_score", curie=MIXS.VOCAB.curie('contam_score'),
                   model_uri=MIXS.VOCAB.contam_score, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} percentage'))

slots.contam_screen_input = Slot(uri=MIXS.VOCAB.contam_screen_input, name="contam_screen_input", curie=MIXS.VOCAB.curie('contam_screen_input'),
                   model_uri=MIXS.VOCAB.contam_screen_input, domain=None, range=Optional[str],
                   pattern=re.compile(r'[reads| contigs]'))

slots.contam_screen_param = Slot(uri=MIXS.VOCAB.contam_screen_param, name="contam_screen_param", curie=MIXS.VOCAB.curie('contam_screen_param'),
                   model_uri=MIXS.VOCAB.contam_screen_param, domain=None, range=Optional[str],
                   pattern=re.compile(r'[ref db|kmer|coverage|combination];{text|integer}'))

slots.decontam_software = Slot(uri=MIXS.VOCAB.decontam_software, name="decontam_software", curie=MIXS.VOCAB.curie('decontam_software'),
                   model_uri=MIXS.VOCAB.decontam_software, domain=None, range=Optional[str],
                   pattern=re.compile(r'[checkm/refinem|anvi'o|prodege|bbtools:decontaminate.sh|acdc|combination]'))

slots.sort_tech = Slot(uri=MIXS.VOCAB.sort_tech, name="sort_tech", curie=MIXS.VOCAB.curie('sort_tech'),
                   model_uri=MIXS.VOCAB.sort_tech, domain=None, range=Optional[str],
                   pattern=re.compile(r'[flow cytometric cell sorting|microfluidics|lazer-tweezing|optical manipulation|micromanipulation|other]'))

slots.single_cell_lysis_appr = Slot(uri=MIXS.VOCAB.single_cell_lysis_appr, name="single_cell_lysis_appr", curie=MIXS.VOCAB.curie('single_cell_lysis_appr'),
                   model_uri=MIXS.VOCAB.single_cell_lysis_appr, domain=None, range=Optional[str],
                   pattern=re.compile(r'[chemical|enzymatic|physical|combination]'))

slots.single_cell_lysis_prot = Slot(uri=MIXS.VOCAB.single_cell_lysis_prot, name="single_cell_lysis_prot", curie=MIXS.VOCAB.curie('single_cell_lysis_prot'),
                   model_uri=MIXS.VOCAB.single_cell_lysis_prot, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.wga_amp_appr = Slot(uri=MIXS.VOCAB.wga_amp_appr, name="wga_amp_appr", curie=MIXS.VOCAB.curie('wga_amp_appr'),
                   model_uri=MIXS.VOCAB.wga_amp_appr, domain=None, range=Optional[str],
                   pattern=re.compile(r'[pcr based|mda based]'))

slots.wga_amp_kit = Slot(uri=MIXS.VOCAB.wga_amp_kit, name="wga_amp_kit", curie=MIXS.VOCAB.curie('wga_amp_kit'),
                   model_uri=MIXS.VOCAB.wga_amp_kit, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.bin_param = Slot(uri=MIXS.VOCAB.bin_param, name="bin_param", curie=MIXS.VOCAB.curie('bin_param'),
                   model_uri=MIXS.VOCAB.bin_param, domain=None, range=Optional[str],
                   pattern=re.compile(r'[homology search|kmer|coverage|codon usage|combination]'))

slots.bin_software = Slot(uri=MIXS.VOCAB.bin_software, name="bin_software", curie=MIXS.VOCAB.curie('bin_software'),
                   model_uri=MIXS.VOCAB.bin_software, domain=None, range=Optional[str],
                   pattern=re.compile(r'[metabat|maxbin|concoct|groupm|esom|metawatt|combination|other]'))

slots.reassembly_bin = Slot(uri=MIXS.VOCAB.reassembly_bin, name="reassembly_bin", curie=MIXS.VOCAB.curie('reassembly_bin'),
                   model_uri=MIXS.VOCAB.reassembly_bin, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean}'))

slots.mag_cov_software = Slot(uri=MIXS.VOCAB.mag_cov_software, name="mag_cov_software", curie=MIXS.VOCAB.curie('mag_cov_software'),
                   model_uri=MIXS.VOCAB.mag_cov_software, domain=None, range=Optional[str],
                   pattern=re.compile(r'[bwa|bbmap|bowtie|other]'))

slots.vir_ident_software = Slot(uri=MIXS.VOCAB.vir_ident_software, name="vir_ident_software", curie=MIXS.VOCAB.curie('vir_ident_software'),
                   model_uri=MIXS.VOCAB.vir_ident_software, domain=None, range=Optional[str],
                   pattern=re.compile(r'{software};{version};{parameters}'))

slots.pred_genome_type = Slot(uri=MIXS.VOCAB.pred_genome_type, name="pred_genome_type", curie=MIXS.VOCAB.curie('pred_genome_type'),
                   model_uri=MIXS.VOCAB.pred_genome_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[DNA|dsDNA|ssDNA|RNA|dsRNA|ssRNA|ssRNA (+)|ssRNA (-)|mixed|uncharacterized]'))

slots.pred_genome_struc = Slot(uri=MIXS.VOCAB.pred_genome_struc, name="pred_genome_struc", curie=MIXS.VOCAB.curie('pred_genome_struc'),
                   model_uri=MIXS.VOCAB.pred_genome_struc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[segmented|non-segmented|undetermined]'))

slots.detec_type = Slot(uri=MIXS.VOCAB.detec_type, name="detec_type", curie=MIXS.VOCAB.curie('detec_type'),
                   model_uri=MIXS.VOCAB.detec_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[independent sequence (UViG)|provirus (UpViG)]'))

slots.votu_class_appr = Slot(uri=MIXS.VOCAB.votu_class_appr, name="votu_class_appr", curie=MIXS.VOCAB.curie('votu_class_appr'),
                   model_uri=MIXS.VOCAB.votu_class_appr, domain=None, range=Optional[str],
                   pattern=re.compile(r'{ANI cutoff};{AF cutoff};{clustering method}'))

slots.votu_seq_comp_appr = Slot(uri=MIXS.VOCAB.votu_seq_comp_appr, name="votu_seq_comp_appr", curie=MIXS.VOCAB.curie('votu_seq_comp_appr'),
                   model_uri=MIXS.VOCAB.votu_seq_comp_appr, domain=None, range=Optional[str],
                   pattern=re.compile(r'{software};{version};{parameters}'))

slots.votu_db = Slot(uri=MIXS.VOCAB.votu_db, name="votu_db", curie=MIXS.VOCAB.curie('votu_db'),
                   model_uri=MIXS.VOCAB.votu_db, domain=None, range=Optional[str],
                   pattern=re.compile(r'{database};{version}'))

slots.host_pred_appr = Slot(uri=MIXS.VOCAB.host_pred_appr, name="host_pred_appr", curie=MIXS.VOCAB.curie('host_pred_appr'),
                   model_uri=MIXS.VOCAB.host_pred_appr, domain=None, range=Optional[str],
                   pattern=re.compile(r'[provirus|host sequence similarity|CRISPR spacer match|kmer similarity|co-occurrence|combination|other]'))

slots.host_pred_est_acc = Slot(uri=MIXS.VOCAB.host_pred_est_acc, name="host_pred_est_acc", curie=MIXS.VOCAB.curie('host_pred_est_acc'),
                   model_uri=MIXS.VOCAB.host_pred_est_acc, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.url = Slot(uri=MIXS.VOCAB.url, name="url", curie=MIXS.VOCAB.curie('url'),
                   model_uri=MIXS.VOCAB.url, domain=None, range=Optional[str],
                   pattern=re.compile(r'{URL}'))

slots.sop = Slot(uri=MIXS.VOCAB.sop, name="sop", curie=MIXS.VOCAB.curie('sop'),
                   model_uri=MIXS.VOCAB.sop, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.barometric_press = Slot(uri=MIXS['0000096'], name="barometric_press", curie=MIXS.curie('0000096'),
                   model_uri=MIXS.VOCAB.barometric_press, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.carb_dioxide = Slot(uri=MIXS['0000097'], name="carb_dioxide", curie=MIXS.curie('0000097'),
                   model_uri=MIXS.VOCAB.carb_dioxide, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.carb_monoxide = Slot(uri=MIXS['0000098'], name="carb_monoxide", curie=MIXS.curie('0000098'),
                   model_uri=MIXS.VOCAB.carb_monoxide, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.chem_administration = Slot(uri=MIXS['0000751'], name="chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=MIXS.VOCAB.chem_administration, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]};{timestamp}'))

slots.humidity = Slot(uri=MIXS['0000100'], name="humidity", curie=MIXS.curie('0000100'),
                   model_uri=MIXS.VOCAB.humidity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.methane = Slot(uri=MIXS['0000101'], name="methane", curie=MIXS.curie('0000101'),
                   model_uri=MIXS.VOCAB.methane, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.misc_param = Slot(uri=MIXS['0000752'], name="misc_param", curie=MIXS.curie('0000752'),
                   model_uri=MIXS.VOCAB.misc_param, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.organism_count = Slot(uri=MIXS['0000103'], name="organism_count", curie=MIXS.curie('0000103'),
                   model_uri=MIXS.VOCAB.organism_count, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};[qPCR|ATP|MPN|other]'))

slots.oxygen = Slot(uri=MIXS['0000104'], name="oxygen", curie=MIXS.curie('0000104'),
                   model_uri=MIXS.VOCAB.oxygen, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.oxy_stat_samp = Slot(uri=MIXS['0000753'], name="oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=MIXS.VOCAB.oxy_stat_samp, domain=None, range=Optional[str],
                   pattern=re.compile(r'[aerobic|anaerobic|other]'))

slots.perturbation = Slot(uri=MIXS['0000754'], name="perturbation", curie=MIXS.curie('0000754'),
                   model_uri=MIXS.VOCAB.perturbation, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{Rn/start_time/end_time/duration}'))

slots.pollutants = Slot(uri=MIXS['0000107'], name="pollutants", curie=MIXS.curie('0000107'),
                   model_uri=MIXS.VOCAB.pollutants, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.resp_part_matter = Slot(uri=MIXS['0000108'], name="resp_part_matter", curie=MIXS.curie('0000108'),
                   model_uri=MIXS.VOCAB.resp_part_matter, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.samp_salinity = Slot(uri=MIXS['0000109'], name="samp_salinity", curie=MIXS.curie('0000109'),
                   model_uri=MIXS.VOCAB.samp_salinity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.samp_store_dur = Slot(uri=MIXS['0000116'], name="samp_store_dur", curie=MIXS.curie('0000116'),
                   model_uri=MIXS.VOCAB.samp_store_dur, domain=None, range=Optional[str],
                   pattern=re.compile(r'{duration}'))

slots.samp_store_loc = Slot(uri=MIXS['0000755'], name="samp_store_loc", curie=MIXS.curie('0000755'),
                   model_uri=MIXS.VOCAB.samp_store_loc, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.samp_store_temp = Slot(uri=MIXS['0000110'], name="samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=MIXS.VOCAB.samp_store_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.samp_vol_we_dna_ext = Slot(uri=MIXS['0000111'], name="samp_vol_we_dna_ext", curie=MIXS.curie('0000111'),
                   model_uri=MIXS.VOCAB.samp_vol_we_dna_ext, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.solar_irradiance = Slot(uri=MIXS['0000112'], name="solar_irradiance", curie=MIXS.curie('0000112'),
                   model_uri=MIXS.VOCAB.solar_irradiance, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.temp = Slot(uri=MIXS['0000113'], name="temp", curie=MIXS.curie('0000113'),
                   model_uri=MIXS.VOCAB.temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.ventilation_rate = Slot(uri=MIXS['0000114'], name="ventilation_rate", curie=MIXS.curie('0000114'),
                   model_uri=MIXS.VOCAB.ventilation_rate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.ventilation_type = Slot(uri=MIXS['0000756'], name="ventilation_type", curie=MIXS.curie('0000756'),
                   model_uri=MIXS.VOCAB.ventilation_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.volatile_org_comp = Slot(uri=MIXS['0000115'], name="volatile_org_comp", curie=MIXS.curie('0000115'),
                   model_uri=MIXS.VOCAB.volatile_org_comp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.wind_direction = Slot(uri=MIXS['0000757'], name="wind_direction", curie=MIXS.curie('0000757'),
                   model_uri=MIXS.VOCAB.wind_direction, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.wind_speed = Slot(uri=MIXS['0000118'], name="wind_speed", curie=MIXS.curie('0000118'),
                   model_uri=MIXS.VOCAB.wind_speed, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.surf_material = Slot(uri=MIXS['0000758'], name="surf_material", curie=MIXS.curie('0000758'),
                   model_uri=MIXS.VOCAB.surf_material, domain=None, range=Optional[str],
                   pattern=re.compile(r'[adobe|carpet|cinder blocks|concrete|hay bales|glass|metal|paint|plastic|stainless steel|stone|stucco|tile|vinyl|wood]'))

slots.surf_air_cont = Slot(uri=MIXS['0000759'], name="surf_air_cont", curie=MIXS.curie('0000759'),
                   model_uri=MIXS.VOCAB.surf_air_cont, domain=None, range=Optional[str],
                   pattern=re.compile(r'[dust|organic matter|particulate matter|volatile organic compounds|biological contaminants|radon|nutrients|biocides]'))

slots.rel_air_humidity = Slot(uri=MIXS['0000121'], name="rel_air_humidity", curie=MIXS.curie('0000121'),
                   model_uri=MIXS.VOCAB.rel_air_humidity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.abs_air_humidity = Slot(uri=MIXS['0000122'], name="abs_air_humidity", curie=MIXS.curie('0000122'),
                   model_uri=MIXS.VOCAB.abs_air_humidity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.surf_humidity = Slot(uri=MIXS['0000123'], name="surf_humidity", curie=MIXS.curie('0000123'),
                   model_uri=MIXS.VOCAB.surf_humidity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.air_temp = Slot(uri=MIXS['0000124'], name="air_temp", curie=MIXS.curie('0000124'),
                   model_uri=MIXS.VOCAB.air_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.surf_temp = Slot(uri=MIXS['0000125'], name="surf_temp", curie=MIXS.curie('0000125'),
                   model_uri=MIXS.VOCAB.surf_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.surf_moisture_ph = Slot(uri=MIXS['0000760'], name="surf_moisture_ph", curie=MIXS.curie('0000760'),
                   model_uri=MIXS.VOCAB.surf_moisture_ph, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float}'))

slots.build_occup_type = Slot(uri=MIXS['0000761'], name="build_occup_type", curie=MIXS.curie('0000761'),
                   model_uri=MIXS.VOCAB.build_occup_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[office|market|restaurant|residence|school|residential|commercial|low rise|high rise|wood framed|office|health care|school|airport|sports complex]'))

slots.surf_moisture = Slot(uri=MIXS['0000128'], name="surf_moisture", curie=MIXS.curie('0000128'),
                   model_uri=MIXS.VOCAB.surf_moisture, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.dew_point = Slot(uri=MIXS['0000129'], name="dew_point", curie=MIXS.curie('0000129'),
                   model_uri=MIXS.VOCAB.dew_point, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.indoor_space = Slot(uri=MIXS['0000763'], name="indoor_space", curie=MIXS.curie('0000763'),
                   model_uri=MIXS.VOCAB.indoor_space, domain=None, range=Optional[str],
                   pattern=re.compile(r'[bedroom|office|bathroom|foyer|kitchen|locker room|hallway|elevator]'))

slots.indoor_surf = Slot(uri=MIXS['0000764'], name="indoor_surf", curie=MIXS.curie('0000764'),
                   model_uri=MIXS.VOCAB.indoor_surf, domain=None, range=Optional[str],
                   pattern=re.compile(r'[cabinet|ceiling|counter top|door|shelving|vent cover|window|wall]'))

slots.filter_type = Slot(uri=MIXS['0000765'], name="filter_type", curie=MIXS.curie('0000765'),
                   model_uri=MIXS.VOCAB.filter_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[particulate air filter|chemical air filter|low-MERV pleated media|HEPA|electrostatic|gas-phase or ultraviolet air treatments]'))

slots.heat_cool_type = Slot(uri=MIXS['0000766'], name="heat_cool_type", curie=MIXS.curie('0000766'),
                   model_uri=MIXS.VOCAB.heat_cool_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[radiant system|heat pump|forced air system|steam forced heat|wood stove]'))

slots.substructure_type = Slot(uri=MIXS['0000767'], name="substructure_type", curie=MIXS.curie('0000767'),
                   model_uri=MIXS.VOCAB.substructure_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[crawlspace|slab on grade|basement]'))

slots.building_setting = Slot(uri=MIXS['0000768'], name="building_setting", curie=MIXS.curie('0000768'),
                   model_uri=MIXS.VOCAB.building_setting, domain=None, range=Optional[str],
                   pattern=re.compile(r'[urban|suburban|exurban|rural]'))

slots.light_type = Slot(uri=MIXS['0000769'], name="light_type", curie=MIXS.curie('0000769'),
                   model_uri=MIXS.VOCAB.light_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[natural light|electric light|desk lamp|flourescent lights|natural light|none]'))

slots.samp_sort_meth = Slot(uri=MIXS['0000216'], name="samp_sort_meth", curie=MIXS.curie('0000216'),
                   model_uri=MIXS.VOCAB.samp_sort_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.space_typ_state = Slot(uri=MIXS['0000770'], name="space_typ_state", curie=MIXS.curie('0000770'),
                   model_uri=MIXS.VOCAB.space_typ_state, domain=None, range=Optional[str],
                   pattern=re.compile(r'[typically occupied|typically unoccupied]'))

slots.typ_occup_density = Slot(uri=MIXS['0000771'], name="typ_occup_density", curie=MIXS.curie('0000771'),
                   model_uri=MIXS.VOCAB.typ_occup_density, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float}'))

slots.occup_samp = Slot(uri=MIXS['0000772'], name="occup_samp", curie=MIXS.curie('0000772'),
                   model_uri=MIXS.VOCAB.occup_samp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.occup_density_samp = Slot(uri=MIXS['0000217'], name="occup_density_samp", curie=MIXS.curie('0000217'),
                   model_uri=MIXS.VOCAB.occup_density_samp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float}'))

slots.address = Slot(uri=MIXS['0000218'], name="address", curie=MIXS.curie('0000218'),
                   model_uri=MIXS.VOCAB.address, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}{text}'))

slots.adj_room = Slot(uri=MIXS['0000219'], name="adj_room", curie=MIXS.curie('0000219'),
                   model_uri=MIXS.VOCAB.adj_room, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{integer}'))

slots.aero_struc = Slot(uri=MIXS['0000773'], name="aero_struc", curie=MIXS.curie('0000773'),
                   model_uri=MIXS.VOCAB.aero_struc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[plane|glider]'))

slots.amount_light = Slot(uri=MIXS['0000140'], name="amount_light", curie=MIXS.curie('0000140'),
                   model_uri=MIXS.VOCAB.amount_light, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.arch_struc = Slot(uri=MIXS['0000774'], name="arch_struc", curie=MIXS.curie('0000774'),
                   model_uri=MIXS.VOCAB.arch_struc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[building|shed|home]'))

slots.avg_occup = Slot(uri=MIXS['0000775'], name="avg_occup", curie=MIXS.curie('0000775'),
                   model_uri=MIXS.VOCAB.avg_occup, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float}'))

slots.avg_dew_point = Slot(uri=MIXS['0000141'], name="avg_dew_point", curie=MIXS.curie('0000141'),
                   model_uri=MIXS.VOCAB.avg_dew_point, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.avg_temp = Slot(uri=MIXS['0000142'], name="avg_temp", curie=MIXS.curie('0000142'),
                   model_uri=MIXS.VOCAB.avg_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.bathroom_count = Slot(uri=MIXS['0000776'], name="bathroom_count", curie=MIXS.curie('0000776'),
                   model_uri=MIXS.VOCAB.bathroom_count, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.bedroom_count = Slot(uri=MIXS['0000777'], name="bedroom_count", curie=MIXS.curie('0000777'),
                   model_uri=MIXS.VOCAB.bedroom_count, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.built_struc_age = Slot(uri=MIXS['0000145'], name="built_struc_age", curie=MIXS.curie('0000145'),
                   model_uri=MIXS.VOCAB.built_struc_age, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.built_struc_set = Slot(uri=MIXS['0000778'], name="built_struc_set", curie=MIXS.curie('0000778'),
                   model_uri=MIXS.VOCAB.built_struc_set, domain=None, range=Optional[str],
                   pattern=re.compile(r'[urban|rural]'))

slots.built_struc_type = Slot(uri=MIXS['0000721'], name="built_struc_type", curie=MIXS.curie('0000721'),
                   model_uri=MIXS.VOCAB.built_struc_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.ceil_area = Slot(uri=MIXS['0000148'], name="ceil_area", curie=MIXS.curie('0000148'),
                   model_uri=MIXS.VOCAB.ceil_area, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.ceil_cond = Slot(uri=MIXS['0000779'], name="ceil_cond", curie=MIXS.curie('0000779'),
                   model_uri=MIXS.VOCAB.ceil_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture]'))

slots.ceil_finish_mat = Slot(uri=MIXS['0000780'], name="ceil_finish_mat", curie=MIXS.curie('0000780'),
                   model_uri=MIXS.VOCAB.ceil_finish_mat, domain=None, range=Optional[str],
                   pattern=re.compile(r'[drywall|mineral fibre|tiles|PVC|plasterboard|metal|fiberglass|stucco|mineral wool/calcium silicate|wood]'))

slots.ceil_water_mold = Slot(uri=MIXS['0000781'], name="ceil_water_mold", curie=MIXS.curie('0000781'),
                   model_uri=MIXS.VOCAB.ceil_water_mold, domain=None, range=Optional[str],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.ceil_struc = Slot(uri=MIXS['0000782'], name="ceil_struc", curie=MIXS.curie('0000782'),
                   model_uri=MIXS.VOCAB.ceil_struc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[wood frame|concrete]'))

slots.ceil_texture = Slot(uri=MIXS['0000783'], name="ceil_texture", curie=MIXS.curie('0000783'),
                   model_uri=MIXS.VOCAB.ceil_texture, domain=None, range=Optional[str],
                   pattern=re.compile(r'[crows feet|crows-foot stomp|double skip|hawk and trowel|knockdown|popcorn|orange peel|rosebud stomp|Santa-Fe texture|skip trowel|smooth|stomp knockdown|swirl]'))

slots.ceil_thermal_mass = Slot(uri=MIXS['0000143'], name="ceil_thermal_mass", curie=MIXS.curie('0000143'),
                   model_uri=MIXS.VOCAB.ceil_thermal_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.ceil_type = Slot(uri=MIXS['0000784'], name="ceil_type", curie=MIXS.curie('0000784'),
                   model_uri=MIXS.VOCAB.ceil_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[cathedral|dropped|concave|barrel-shaped|coffered|cove|stretched]'))

slots.cool_syst_id = Slot(uri=MIXS['0000785'], name="cool_syst_id", curie=MIXS.curie('0000785'),
                   model_uri=MIXS.VOCAB.cool_syst_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.date_last_rain = Slot(uri=MIXS['0000786'], name="date_last_rain", curie=MIXS.curie('0000786'),
                   model_uri=MIXS.VOCAB.date_last_rain, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.build_docs = Slot(uri=MIXS['0000787'], name="build_docs", curie=MIXS.curie('0000787'),
                   model_uri=MIXS.VOCAB.build_docs, domain=None, range=Optional[str],
                   pattern=re.compile(r'[building information model|commissioning report|complaint logs|contract administration|cost estimate|janitorial schedules or logs|maintenance plans|schedule|sections|shop drawings|submittals|ventilation system|windows]'))

slots.door_size = Slot(uri=MIXS['0000158'], name="door_size", curie=MIXS.curie('0000158'),
                   model_uri=MIXS.VOCAB.door_size, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.door_cond = Slot(uri=MIXS['0000788'], name="door_cond", curie=MIXS.curie('0000788'),
                   model_uri=MIXS.VOCAB.door_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'[damaged|needs repair|new|rupture|visible wear]'))

slots.door_direct = Slot(uri=MIXS['0000789'], name="door_direct", curie=MIXS.curie('0000789'),
                   model_uri=MIXS.VOCAB.door_direct, domain=None, range=Optional[str],
                   pattern=re.compile(r'[inward|outward|sideways]'))

slots.door_loc = Slot(uri=MIXS['0000790'], name="door_loc", curie=MIXS.curie('0000790'),
                   model_uri=MIXS.VOCAB.door_loc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.door_mat = Slot(uri=MIXS['0000791'], name="door_mat", curie=MIXS.curie('0000791'),
                   model_uri=MIXS.VOCAB.door_mat, domain=None, range=Optional[str],
                   pattern=re.compile(r'[aluminum|cellular PVC|engineered plastic|fiberboard|fiberglass|metal|thermoplastic alloy|vinyl|wood|wood/plastic composite]'))

slots.door_move = Slot(uri=MIXS['0000792'], name="door_move", curie=MIXS.curie('0000792'),
                   model_uri=MIXS.VOCAB.door_move, domain=None, range=Optional[str],
                   pattern=re.compile(r'[collapsible|folding|revolving|rolling shutter|sliding|swinging]'))

slots.door_water_mold = Slot(uri=MIXS['0000793'], name="door_water_mold", curie=MIXS.curie('0000793'),
                   model_uri=MIXS.VOCAB.door_water_mold, domain=None, range=Optional[str],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.door_type = Slot(uri=MIXS['0000794'], name="door_type", curie=MIXS.curie('0000794'),
                   model_uri=MIXS.VOCAB.door_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[composite|metal|wooden]'))

slots.door_comp_type = Slot(uri=MIXS['0000795'], name="door_comp_type", curie=MIXS.curie('0000795'),
                   model_uri=MIXS.VOCAB.door_comp_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[metal covered|revolving|sliding|telescopic]'))

slots.door_type_metal = Slot(uri=MIXS['0000796'], name="door_type_metal", curie=MIXS.curie('0000796'),
                   model_uri=MIXS.VOCAB.door_type_metal, domain=None, range=Optional[str],
                   pattern=re.compile(r'[collapsible|corrugated steel|hollow|rolling shutters|steel plate]'))

slots.door_type_wood = Slot(uri=MIXS['0000797'], name="door_type_wood", curie=MIXS.curie('0000797'),
                   model_uri=MIXS.VOCAB.door_type_wood, domain=None, range=Optional[str],
                   pattern=re.compile(r'[bettened and ledged|battened|ledged and braced|battened|ledged and framed|battened|ledged, braced and frame|framed and paneled|glashed or sash|flush|louvered|wire gauged]'))

slots.drawings = Slot(uri=MIXS['0000798'], name="drawings", curie=MIXS.curie('0000798'),
                   model_uri=MIXS.VOCAB.drawings, domain=None, range=Optional[str],
                   pattern=re.compile(r'[operation|as built|construction|bid|design|building navigation map|diagram|sketch]'))

slots.elevator = Slot(uri=MIXS['0000799'], name="elevator", curie=MIXS.curie('0000799'),
                   model_uri=MIXS.VOCAB.elevator, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.escalator = Slot(uri=MIXS['0000800'], name="escalator", curie=MIXS.curie('0000800'),
                   model_uri=MIXS.VOCAB.escalator, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.exp_duct = Slot(uri=MIXS['0000144'], name="exp_duct", curie=MIXS.curie('0000144'),
                   model_uri=MIXS.VOCAB.exp_duct, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.exp_pipe = Slot(uri=MIXS['0000220'], name="exp_pipe", curie=MIXS.curie('0000220'),
                   model_uri=MIXS.VOCAB.exp_pipe, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.ext_door = Slot(uri=MIXS['0000170'], name="ext_door", curie=MIXS.curie('0000170'),
                   model_uri=MIXS.VOCAB.ext_door, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.fireplace_type = Slot(uri=MIXS['0000802'], name="fireplace_type", curie=MIXS.curie('0000802'),
                   model_uri=MIXS.VOCAB.fireplace_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[gas burning|wood burning]'))

slots.floor_age = Slot(uri=MIXS['0000164'], name="floor_age", curie=MIXS.curie('0000164'),
                   model_uri=MIXS.VOCAB.floor_age, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.floor_area = Slot(uri=MIXS['0000165'], name="floor_area", curie=MIXS.curie('0000165'),
                   model_uri=MIXS.VOCAB.floor_area, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.floor_cond = Slot(uri=MIXS['0000803'], name="floor_cond", curie=MIXS.curie('0000803'),
                   model_uri=MIXS.VOCAB.floor_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture]'))

slots.floor_count = Slot(uri=MIXS['0000225'], name="floor_count", curie=MIXS.curie('0000225'),
                   model_uri=MIXS.VOCAB.floor_count, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.floor_finish_mat = Slot(uri=MIXS['0000804'], name="floor_finish_mat", curie=MIXS.curie('0000804'),
                   model_uri=MIXS.VOCAB.floor_finish_mat, domain=None, range=Optional[str],
                   pattern=re.compile(r'[tile|wood strip or parquet|carpet|rug|laminate wood|lineoleum|vinyl composition tile|sheet vinyl|stone|bamboo|cork|terrazo|concrete|none;specify unfinished|sealed|clear finish|paint]'))

slots.floor_water_mold = Slot(uri=MIXS['0000805'], name="floor_water_mold", curie=MIXS.curie('0000805'),
                   model_uri=MIXS.VOCAB.floor_water_mold, domain=None, range=Optional[str],
                   pattern=re.compile(r'[mold odor|wet floor|water stains|wall discoloration|floor discoloration|ceiling discoloration|peeling paint or wallpaper|bulging walls|condensation]'))

slots.floor_struc = Slot(uri=MIXS['0000806'], name="floor_struc", curie=MIXS.curie('0000806'),
                   model_uri=MIXS.VOCAB.floor_struc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[balcony|floating floor|glass floor|raised floor|sprung floor|wood-framed|concrete]'))

slots.floor_thermal_mass = Slot(uri=MIXS['0000166'], name="floor_thermal_mass", curie=MIXS.curie('0000166'),
                   model_uri=MIXS.VOCAB.floor_thermal_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.freq_clean = Slot(uri=MIXS['0000226'], name="freq_clean", curie=MIXS.curie('0000226'),
                   model_uri=MIXS.VOCAB.freq_clean, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.freq_cook = Slot(uri=MIXS['0000227'], name="freq_cook", curie=MIXS.curie('0000227'),
                   model_uri=MIXS.VOCAB.freq_cook, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.furniture = Slot(uri=MIXS['0000807'], name="furniture", curie=MIXS.curie('0000807'),
                   model_uri=MIXS.VOCAB.furniture, domain=None, range=Optional[str],
                   pattern=re.compile(r'[cabinet|chair|desks]'))

slots.gender_restroom = Slot(uri=MIXS['0000808'], name="gender_restroom", curie=MIXS.curie('0000808'),
                   model_uri=MIXS.VOCAB.gender_restroom, domain=None, range=Optional[str],
                   pattern=re.compile(r'[male|female]'))

slots.hall_count = Slot(uri=MIXS['0000228'], name="hall_count", curie=MIXS.curie('0000228'),
                   model_uri=MIXS.VOCAB.hall_count, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.handidness = Slot(uri=MIXS['0000809'], name="handidness", curie=MIXS.curie('0000809'),
                   model_uri=MIXS.VOCAB.handidness, domain=None, range=Optional[str],
                   pattern=re.compile(r'[ambidexterity|left handedness|mixed-handedness|right handedness]'))

slots.heat_deliv_loc = Slot(uri=MIXS['0000810'], name="heat_deliv_loc", curie=MIXS.curie('0000810'),
                   model_uri=MIXS.VOCAB.heat_deliv_loc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.heat_system_deliv_meth = Slot(uri=MIXS['0000812'], name="heat_system_deliv_meth", curie=MIXS.curie('0000812'),
                   model_uri=MIXS.VOCAB.heat_system_deliv_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'[conductive|radiant]'))

slots.heat_system_id = Slot(uri=MIXS['0000833'], name="heat_system_id", curie=MIXS.curie('0000833'),
                   model_uri=MIXS.VOCAB.heat_system_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.height_carper_fiber = Slot(uri=MIXS['0000167'], name="height_carper_fiber", curie=MIXS.curie('0000167'),
                   model_uri=MIXS.VOCAB.height_carper_fiber, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.inside_lux = Slot(uri=MIXS['0000168'], name="inside_lux", curie=MIXS.curie('0000168'),
                   model_uri=MIXS.VOCAB.inside_lux, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.int_wall_cond = Slot(uri=MIXS['0000813'], name="int_wall_cond", curie=MIXS.curie('0000813'),
                   model_uri=MIXS.VOCAB.int_wall_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture]'))

slots.last_clean = Slot(uri=MIXS['0000814'], name="last_clean", curie=MIXS.curie('0000814'),
                   model_uri=MIXS.VOCAB.last_clean, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.max_occup = Slot(uri=MIXS['0000229'], name="max_occup", curie=MIXS.curie('0000229'),
                   model_uri=MIXS.VOCAB.max_occup, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.mech_struc = Slot(uri=MIXS['0000815'], name="mech_struc", curie=MIXS.curie('0000815'),
                   model_uri=MIXS.VOCAB.mech_struc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[subway|coach|carriage|elevator|escalator|boat|train|car|bus]'))

slots.number_plants = Slot(uri=MIXS['0000230'], name="number_plants", curie=MIXS.curie('0000230'),
                   model_uri=MIXS.VOCAB.number_plants, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.number_pets = Slot(uri=MIXS['0000231'], name="number_pets", curie=MIXS.curie('0000231'),
                   model_uri=MIXS.VOCAB.number_pets, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.number_resident = Slot(uri=MIXS['0000232'], name="number_resident", curie=MIXS.curie('0000232'),
                   model_uri=MIXS.VOCAB.number_resident, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.occup_document = Slot(uri=MIXS['0000816'], name="occup_document", curie=MIXS.curie('0000816'),
                   model_uri=MIXS.VOCAB.occup_document, domain=None, range=Optional[str],
                   pattern=re.compile(r'[automated count|estimate|manual count|videos]'))

slots.ext_wall_orient = Slot(uri=MIXS['0000817'], name="ext_wall_orient", curie=MIXS.curie('0000817'),
                   model_uri=MIXS.VOCAB.ext_wall_orient, domain=None, range=Optional[str],
                   pattern=re.compile(r'[north|south|east|west|northeast|southeast|southwest|northwest]'))

slots.ext_window_orient = Slot(uri=MIXS['0000818'], name="ext_window_orient", curie=MIXS.curie('0000818'),
                   model_uri=MIXS.VOCAB.ext_window_orient, domain=None, range=Optional[str],
                   pattern=re.compile(r'[north|south|east|west|northeast|southeast|southwest|northwest]'))

slots.rel_humidity_out = Slot(uri=MIXS['0000188'], name="rel_humidity_out", curie=MIXS.curie('0000188'),
                   model_uri=MIXS.VOCAB.rel_humidity_out, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.pres_animal = Slot(uri=MIXS['0000819'], name="pres_animal", curie=MIXS.curie('0000819'),
                   model_uri=MIXS.VOCAB.pres_animal, domain=None, range=Optional[str],
                   pattern=re.compile(r'[cat|dog|rodent|snake|other];{integer}'))

slots.quad_pos = Slot(uri=MIXS['0000820'], name="quad_pos", curie=MIXS.curie('0000820'),
                   model_uri=MIXS.VOCAB.quad_pos, domain=None, range=Optional[str],
                   pattern=re.compile(r'[North side|West side|South side|East side]'))

slots.rel_samp_loc = Slot(uri=MIXS['0000821'], name="rel_samp_loc", curie=MIXS.curie('0000821'),
                   model_uri=MIXS.VOCAB.rel_samp_loc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[edge of car|center of car|under a seat]'))

slots.room_air_exch_rate = Slot(uri=MIXS['0000169'], name="room_air_exch_rate", curie=MIXS.curie('0000169'),
                   model_uri=MIXS.VOCAB.room_air_exch_rate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.room_architec_element = Slot(uri=MIXS['0000233'], name="room_architec_element", curie=MIXS.curie('0000233'),
                   model_uri=MIXS.VOCAB.room_architec_element, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.room_condt = Slot(uri=MIXS['0000822'], name="room_condt", curie=MIXS.curie('0000822'),
                   model_uri=MIXS.VOCAB.room_condt, domain=None, range=Optional[str],
                   pattern=re.compile(r'[new|visible wear|needs repair|damaged|rupture|visible signs of mold/mildew]'))

slots.room_count = Slot(uri=MIXS['0000234'], name="room_count", curie=MIXS.curie('0000234'),
                   model_uri=MIXS.VOCAB.room_count, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.room_dim = Slot(uri=MIXS['0000192'], name="room_dim", curie=MIXS.curie('0000192'),
                   model_uri=MIXS.VOCAB.room_dim, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer} {unit} x {integer} {unit} x {integer} {unit}'))

slots.room_door_dist = Slot(uri=MIXS['0000193'], name="room_door_dist", curie=MIXS.curie('0000193'),
                   model_uri=MIXS.VOCAB.room_door_dist, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer} {unit}'))

slots.room_loc = Slot(uri=MIXS['0000823'], name="room_loc", curie=MIXS.curie('0000823'),
                   model_uri=MIXS.VOCAB.room_loc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[corner room|interior room|exterior wall]'))

slots.room_moist_damage_hist = Slot(uri=MIXS['0000235'], name="room_moist_damage_hist", curie=MIXS.curie('0000235'),
                   model_uri=MIXS.VOCAB.room_moist_damage_hist, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.room_net_area = Slot(uri=MIXS['0000194'], name="room_net_area", curie=MIXS.curie('0000194'),
                   model_uri=MIXS.VOCAB.room_net_area, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer} {unit}'))

slots.room_occup = Slot(uri=MIXS['0000236'], name="room_occup", curie=MIXS.curie('0000236'),
                   model_uri=MIXS.VOCAB.room_occup, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.room_samp_pos = Slot(uri=MIXS['0000824'], name="room_samp_pos", curie=MIXS.curie('0000824'),
                   model_uri=MIXS.VOCAB.room_samp_pos, domain=None, range=Optional[str],
                   pattern=re.compile(r'[north corner|south corner|west corner|east corner|northeast corner|northwest corner|southeast corner|southwest corner|center]'))

slots.room_type = Slot(uri=MIXS['0000825'], name="room_type", curie=MIXS.curie('0000825'),
                   model_uri=MIXS.VOCAB.room_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[attic|bathroom|closet|conference room|elevator|examining room|hallway|kitchen|mail room|private office|open office|stairwell|,restroom|lobby|vestibule|mechanical or electrical room|data center|laboratory_wet|laboratory_dry|gymnasium|natatorium|auditorium|lockers|cafe|warehouse]'))

slots.room_vol = Slot(uri=MIXS['0000195'], name="room_vol", curie=MIXS.curie('0000195'),
                   model_uri=MIXS.VOCAB.room_vol, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer} {unit}'))

slots.room_window_count = Slot(uri=MIXS['0000237'], name="room_window_count", curie=MIXS.curie('0000237'),
                   model_uri=MIXS.VOCAB.room_window_count, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.room_connected = Slot(uri=MIXS['0000826'], name="room_connected", curie=MIXS.curie('0000826'),
                   model_uri=MIXS.VOCAB.room_connected, domain=None, range=Optional[str],
                   pattern=re.compile(r'[attic|bathroom|closet|conference room|elevator|examining room|hallway|kitchen|mail room|office|stairwell]'))

slots.room_hallway = Slot(uri=MIXS['0000238'], name="room_hallway", curie=MIXS.curie('0000238'),
                   model_uri=MIXS.VOCAB.room_hallway, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{integer}'))

slots.room_door_share = Slot(uri=MIXS['0000242'], name="room_door_share", curie=MIXS.curie('0000242'),
                   model_uri=MIXS.VOCAB.room_door_share, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{integer}'))

slots.room_wall_share = Slot(uri=MIXS['0000243'], name="room_wall_share", curie=MIXS.curie('0000243'),
                   model_uri=MIXS.VOCAB.room_wall_share, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{integer}'))

slots.samp_weather = Slot(uri=MIXS['0000827'], name="samp_weather", curie=MIXS.curie('0000827'),
                   model_uri=MIXS.VOCAB.samp_weather, domain=None, range=Optional[str],
                   pattern=re.compile(r'[clear sky|cloudy|foggy|hail|rain|snow|sleet|sunny|windy]'))

slots.samp_floor = Slot(uri=MIXS['0000828'], name="samp_floor", curie=MIXS.curie('0000828'),
                   model_uri=MIXS.VOCAB.samp_floor, domain=None, range=Optional[str],
                   pattern=re.compile(r'[1st floor|2nd floor|{integer} floor|basement|lobby]'))

slots.samp_room_id = Slot(uri=MIXS['0000244'], name="samp_room_id", curie=MIXS.curie('0000244'),
                   model_uri=MIXS.VOCAB.samp_room_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.samp_time_out = Slot(uri=MIXS['0000196'], name="samp_time_out", curie=MIXS.curie('0000196'),
                   model_uri=MIXS.VOCAB.samp_time_out, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float}'))

slots.season = Slot(uri=MIXS['0000829'], name="season", curie=MIXS.curie('0000829'),
                   model_uri=MIXS.VOCAB.season, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}'))

slots.season_use = Slot(uri=MIXS['0000830'], name="season_use", curie=MIXS.curie('0000830'),
                   model_uri=MIXS.VOCAB.season_use, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Spring|Summer|Fall|Winter]'))

slots.shading_device_cond = Slot(uri=MIXS['0000831'], name="shading_device_cond", curie=MIXS.curie('0000831'),
                   model_uri=MIXS.VOCAB.shading_device_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'[damaged|needs repair|new|rupture|visible wear]'))

slots.shading_device_loc = Slot(uri=MIXS['0000832'], name="shading_device_loc", curie=MIXS.curie('0000832'),
                   model_uri=MIXS.VOCAB.shading_device_loc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[exterior|interior]'))

slots.shading_device_mat = Slot(uri=MIXS['0000245'], name="shading_device_mat", curie=MIXS.curie('0000245'),
                   model_uri=MIXS.VOCAB.shading_device_mat, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.shading_device_water_mold = Slot(uri=MIXS['0000834'], name="shading_device_water_mold", curie=MIXS.curie('0000834'),
                   model_uri=MIXS.VOCAB.shading_device_water_mold, domain=None, range=Optional[str],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.shading_device_type = Slot(uri=MIXS['0000835'], name="shading_device_type", curie=MIXS.curie('0000835'),
                   model_uri=MIXS.VOCAB.shading_device_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[bahama shutters|exterior roll blind|gambrel awning|hood awning|porchroller awning|sarasota shutters|slatted aluminum|solid aluminum awning|sun screen|tree|trellis|venetian awning]'))

slots.specific_humidity = Slot(uri=MIXS['0000214'], name="specific_humidity", curie=MIXS.curie('0000214'),
                   model_uri=MIXS.VOCAB.specific_humidity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.specific = Slot(uri=MIXS['0000836'], name="specific", curie=MIXS.curie('0000836'),
                   model_uri=MIXS.VOCAB.specific, domain=None, range=Optional[str],
                   pattern=re.compile(r'[operation|as built|construction|bid|design|photos]'))

slots.temp_out = Slot(uri=MIXS['0000197'], name="temp_out", curie=MIXS.curie('0000197'),
                   model_uri=MIXS.VOCAB.temp_out, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.train_line = Slot(uri=MIXS['0000837'], name="train_line", curie=MIXS.curie('0000837'),
                   model_uri=MIXS.VOCAB.train_line, domain=None, range=Optional[str],
                   pattern=re.compile(r'[red|green|orange]'))

slots.train_stat_loc = Slot(uri=MIXS['0000838'], name="train_stat_loc", curie=MIXS.curie('0000838'),
                   model_uri=MIXS.VOCAB.train_stat_loc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[south station above ground|south station underground|south station amtrak|forest hills|riverside]'))

slots.train_stop_loc = Slot(uri=MIXS['0000839'], name="train_stop_loc", curie=MIXS.curie('0000839'),
                   model_uri=MIXS.VOCAB.train_stop_loc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[end|mid|downtown]'))

slots.vis_media = Slot(uri=MIXS['0000840'], name="vis_media", curie=MIXS.curie('0000840'),
                   model_uri=MIXS.VOCAB.vis_media, domain=None, range=Optional[str],
                   pattern=re.compile(r'[photos|videos|commonly of the building|site context (adjacent buildings, vegetation, terrain, streets)|interiors|equipment|3D scans]'))

slots.wall_area = Slot(uri=MIXS['0000198'], name="wall_area", curie=MIXS.curie('0000198'),
                   model_uri=MIXS.VOCAB.wall_area, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.wall_const_type = Slot(uri=MIXS['0000841'], name="wall_const_type", curie=MIXS.curie('0000841'),
                   model_uri=MIXS.VOCAB.wall_const_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[frame construction|joisted masonry|light noncombustible|masonry noncombustible|modified fire resistive|fire resistive]'))

slots.wall_finish_mat = Slot(uri=MIXS['0000842'], name="wall_finish_mat", curie=MIXS.curie('0000842'),
                   model_uri=MIXS.VOCAB.wall_finish_mat, domain=None, range=Optional[str],
                   pattern=re.compile(r'[plaster|gypsum plaster|veneer plaster|gypsum board|tile|terrazzo|stone facing|acoustical treatment|wood|metal|masonry]'))

slots.wall_height = Slot(uri=MIXS['0000221'], name="wall_height", curie=MIXS.curie('0000221'),
                   model_uri=MIXS.VOCAB.wall_height, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.wall_loc = Slot(uri=MIXS['0000843'], name="wall_loc", curie=MIXS.curie('0000843'),
                   model_uri=MIXS.VOCAB.wall_loc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.wall_water_mold = Slot(uri=MIXS['0000844'], name="wall_water_mold", curie=MIXS.curie('0000844'),
                   model_uri=MIXS.VOCAB.wall_water_mold, domain=None, range=Optional[str],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.wall_surf_treatment = Slot(uri=MIXS['0000845'], name="wall_surf_treatment", curie=MIXS.curie('0000845'),
                   model_uri=MIXS.VOCAB.wall_surf_treatment, domain=None, range=Optional[str],
                   pattern=re.compile(r'[painted|wall paper|no treatment|paneling|stucco|fabric]'))

slots.wall_texture = Slot(uri=MIXS['0000846'], name="wall_texture", curie=MIXS.curie('0000846'),
                   model_uri=MIXS.VOCAB.wall_texture, domain=None, range=Optional[str],
                   pattern=re.compile(r'[crows feet|crows-foot stomp||double skip|hawk and trowel|knockdown|popcorn|orange peel|rosebud stomp|Santa-Fe texture|skip trowel|smooth|stomp knockdown|swirl]'))

slots.wall_thermal_mass = Slot(uri=MIXS['0000222'], name="wall_thermal_mass", curie=MIXS.curie('0000222'),
                   model_uri=MIXS.VOCAB.wall_thermal_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.water_feat_size = Slot(uri=MIXS['0000223'], name="water_feat_size", curie=MIXS.curie('0000223'),
                   model_uri=MIXS.VOCAB.water_feat_size, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.water_feat_type = Slot(uri=MIXS['0000847'], name="water_feat_type", curie=MIXS.curie('0000847'),
                   model_uri=MIXS.VOCAB.water_feat_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[fountain|pool|standing feature|stream|waterfall]'))

slots.weekday = Slot(uri=MIXS['0000848'], name="weekday", curie=MIXS.curie('0000848'),
                   model_uri=MIXS.VOCAB.weekday, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday]'))

slots.window_size = Slot(uri=MIXS['0000224'], name="window_size", curie=MIXS.curie('0000224'),
                   model_uri=MIXS.VOCAB.window_size, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit} x {float} {unit}'))

slots.window_cond = Slot(uri=MIXS['0000849'], name="window_cond", curie=MIXS.curie('0000849'),
                   model_uri=MIXS.VOCAB.window_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'[damaged|needs repair|new|rupture|visible wear]'))

slots.window_cover = Slot(uri=MIXS['0000850'], name="window_cover", curie=MIXS.curie('0000850'),
                   model_uri=MIXS.VOCAB.window_cover, domain=None, range=Optional[str],
                   pattern=re.compile(r'[blinds|curtains|none]'))

slots.window_horiz_pos = Slot(uri=MIXS['0000851'], name="window_horiz_pos", curie=MIXS.curie('0000851'),
                   model_uri=MIXS.VOCAB.window_horiz_pos, domain=None, range=Optional[str],
                   pattern=re.compile(r'[left|middle|right]'))

slots.window_loc = Slot(uri=MIXS['0000852'], name="window_loc", curie=MIXS.curie('0000852'),
                   model_uri=MIXS.VOCAB.window_loc, domain=None, range=Optional[str],
                   pattern=re.compile(r'[north|south|east|west]'))

slots.window_mat = Slot(uri=MIXS['0000853'], name="window_mat", curie=MIXS.curie('0000853'),
                   model_uri=MIXS.VOCAB.window_mat, domain=None, range=Optional[str],
                   pattern=re.compile(r'[clad|fiberglass|metal|vinyl|wood]'))

slots.window_open_freq = Slot(uri=MIXS['0000246'], name="window_open_freq", curie=MIXS.curie('0000246'),
                   model_uri=MIXS.VOCAB.window_open_freq, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.window_water_mold = Slot(uri=MIXS['0000854'], name="window_water_mold", curie=MIXS.curie('0000854'),
                   model_uri=MIXS.VOCAB.window_water_mold, domain=None, range=Optional[str],
                   pattern=re.compile(r'[presence of mold visible|no presence of mold visible]'))

slots.window_status = Slot(uri=MIXS['0000855'], name="window_status", curie=MIXS.curie('0000855'),
                   model_uri=MIXS.VOCAB.window_status, domain=None, range=Optional[str],
                   pattern=re.compile(r'[closed|open]'))

slots.window_type = Slot(uri=MIXS['0000856'], name="window_type", curie=MIXS.curie('0000856'),
                   model_uri=MIXS.VOCAB.window_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[single-hung sash window|horizontal sash window|fixed window]'))

slots.window_vert_pos = Slot(uri=MIXS['0000857'], name="window_vert_pos", curie=MIXS.curie('0000857'),
                   model_uri=MIXS.VOCAB.window_vert_pos, domain=None, range=Optional[str],
                   pattern=re.compile(r'[bottom|middle|top|low|middle|high]'))

slots.ances_data = Slot(uri=MIXS['0000247'], name="ances_data", curie=MIXS.curie('0000247'),
                   model_uri=MIXS.VOCAB.ances_data, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.biol_stat = Slot(uri=MIXS['0000858'], name="biol_stat", curie=MIXS.curie('0000858'),
                   model_uri=MIXS.VOCAB.biol_stat, domain=None, range=Optional[str],
                   pattern=re.compile(r'[wild|natural|semi-natural|inbred line|breeder's line|hybrid|clonal selection|mutant]'))

slots.genetic_mod = Slot(uri=MIXS['0000859'], name="genetic_mod", curie=MIXS.curie('0000859'),
                   model_uri=MIXS.VOCAB.genetic_mod, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}|{text}'))

slots.host_common_name = Slot(uri=MIXS['0000248'], name="host_common_name", curie=MIXS.curie('0000248'),
                   model_uri=MIXS.VOCAB.host_common_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.samp_capt_status = Slot(uri=MIXS['0000860'], name="samp_capt_status", curie=MIXS.curie('0000860'),
                   model_uri=MIXS.VOCAB.samp_capt_status, domain=None, range=Optional[str],
                   pattern=re.compile(r'[active surveillance in response to an outbreak|active surveillance not initiated by an outbreak|farm sample|market sample|other]'))

slots.samp_dis_stage = Slot(uri=MIXS['0000249'], name="samp_dis_stage", curie=MIXS.curie('0000249'),
                   model_uri=MIXS.VOCAB.samp_dis_stage, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_taxid = Slot(uri=MIXS['0000250'], name="host_taxid", curie=MIXS.curie('0000250'),
                   model_uri=MIXS.VOCAB.host_taxid, domain=None, range=Optional[str],
                   pattern=re.compile(r'{NCBI taxid}'))

slots.host_subject_id = Slot(uri=MIXS['0000861'], name="host_subject_id", curie=MIXS.curie('0000861'),
                   model_uri=MIXS.VOCAB.host_subject_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_age = Slot(uri=MIXS['0000255'], name="host_age", curie=MIXS.curie('0000255'),
                   model_uri=MIXS.VOCAB.host_age, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.host_life_stage = Slot(uri=MIXS['0000251'], name="host_life_stage", curie=MIXS.curie('0000251'),
                   model_uri=MIXS.VOCAB.host_life_stage, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_sex = Slot(uri=MIXS['0000811'], name="host_sex", curie=MIXS.curie('0000811'),
                   model_uri=MIXS.VOCAB.host_sex, domain=None, range=Optional[str],
                   pattern=re.compile(r'[male|female|neuter|hermaphrodite|not determined]'))

slots.host_disease_stat = Slot(uri=MIXS['0000031'], name="host_disease_stat", curie=MIXS.curie('0000031'),
                   model_uri=MIXS.VOCAB.host_disease_stat, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}|{text}'))

slots.host_body_habitat = Slot(uri=MIXS['0000866'], name="host_body_habitat", curie=MIXS.curie('0000866'),
                   model_uri=MIXS.VOCAB.host_body_habitat, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_body_site = Slot(uri=MIXS['0000867'], name="host_body_site", curie=MIXS.curie('0000867'),
                   model_uri=MIXS.VOCAB.host_body_site, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}'))

slots.host_body_product = Slot(uri=MIXS['0000888'], name="host_body_product", curie=MIXS.curie('0000888'),
                   model_uri=MIXS.VOCAB.host_body_product, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}'))

slots.host_tot_mass = Slot(uri=MIXS['0000263'], name="host_tot_mass", curie=MIXS.curie('0000263'),
                   model_uri=MIXS.VOCAB.host_tot_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.host_height = Slot(uri=MIXS['0000264'], name="host_height", curie=MIXS.curie('0000264'),
                   model_uri=MIXS.VOCAB.host_height, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.host_length = Slot(uri=MIXS['0000256'], name="host_length", curie=MIXS.curie('0000256'),
                   model_uri=MIXS.VOCAB.host_length, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.host_diet = Slot(uri=MIXS['0000869'], name="host_diet", curie=MIXS.curie('0000869'),
                   model_uri=MIXS.VOCAB.host_diet, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_last_meal = Slot(uri=MIXS['0000870'], name="host_last_meal", curie=MIXS.curie('0000870'),
                   model_uri=MIXS.VOCAB.host_last_meal, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{duration}'))

slots.host_growth_cond = Slot(uri=MIXS['0000871'], name="host_growth_cond", curie=MIXS.curie('0000871'),
                   model_uri=MIXS.VOCAB.host_growth_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}|{text}'))

slots.host_substrate = Slot(uri=MIXS['0000252'], name="host_substrate", curie=MIXS.curie('0000252'),
                   model_uri=MIXS.VOCAB.host_substrate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_family_relationship = Slot(uri=MIXS['0000872'], name="host_family_relationship", curie=MIXS.curie('0000872'),
                   model_uri=MIXS.VOCAB.host_family_relationship, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{text}'))

slots.host_infra_specific_name = Slot(uri=MIXS['0000253'], name="host_infra_specific_name", curie=MIXS.curie('0000253'),
                   model_uri=MIXS.VOCAB.host_infra_specific_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_infra_specific_rank = Slot(uri=MIXS['0000254'], name="host_infra_specific_rank", curie=MIXS.curie('0000254'),
                   model_uri=MIXS.VOCAB.host_infra_specific_rank, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_genotype = Slot(uri=MIXS['0000365'], name="host_genotype", curie=MIXS.curie('0000365'),
                   model_uri=MIXS.VOCAB.host_genotype, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_phenotype = Slot(uri=MIXS['0000874'], name="host_phenotype", curie=MIXS.curie('0000874'),
                   model_uri=MIXS.VOCAB.host_phenotype, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}'))

slots.host_body_temp = Slot(uri=MIXS['0000274'], name="host_body_temp", curie=MIXS.curie('0000274'),
                   model_uri=MIXS.VOCAB.host_body_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.host_dry_mass = Slot(uri=MIXS['0000257'], name="host_dry_mass", curie=MIXS.curie('0000257'),
                   model_uri=MIXS.VOCAB.host_dry_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.host_blood_press_diast = Slot(uri=MIXS['0000258'], name="host_blood_press_diast", curie=MIXS.curie('0000258'),
                   model_uri=MIXS.VOCAB.host_blood_press_diast, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.host_blood_press_syst = Slot(uri=MIXS['0000259'], name="host_blood_press_syst", curie=MIXS.curie('0000259'),
                   model_uri=MIXS.VOCAB.host_blood_press_syst, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.host_color = Slot(uri=MIXS['0000260'], name="host_color", curie=MIXS.curie('0000260'),
                   model_uri=MIXS.VOCAB.host_color, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_shape = Slot(uri=MIXS['0000261'], name="host_shape", curie=MIXS.curie('0000261'),
                   model_uri=MIXS.VOCAB.host_shape, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.gravidity = Slot(uri=MIXS['0000875'], name="gravidity", curie=MIXS.curie('0000875'),
                   model_uri=MIXS.VOCAB.gravidity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean};{timestamp}'))

slots.ihmc_medication_code = Slot(uri=MIXS['0000884'], name="ihmc_medication_code", curie=MIXS.curie('0000884'),
                   model_uri=MIXS.VOCAB.ihmc_medication_code, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.smoker = Slot(uri=MIXS['0000262'], name="smoker", curie=MIXS.curie('0000262'),
                   model_uri=MIXS.VOCAB.smoker, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean}'))

slots.host_hiv_stat = Slot(uri=MIXS['0000265'], name="host_hiv_stat", curie=MIXS.curie('0000265'),
                   model_uri=MIXS.VOCAB.host_hiv_stat, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean};{boolean}'))

slots.drug_usage = Slot(uri=MIXS['0000894'], name="drug_usage", curie=MIXS.curie('0000894'),
                   model_uri=MIXS.VOCAB.drug_usage, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{integer}/[year|month|week|day|hour]'))

slots.host_body_mass_index = Slot(uri=MIXS['0000317'], name="host_body_mass_index", curie=MIXS.curie('0000317'),
                   model_uri=MIXS.VOCAB.host_body_mass_index, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diet_last_six_month = Slot(uri=MIXS['0000266'], name="diet_last_six_month", curie=MIXS.curie('0000266'),
                   model_uri=MIXS.VOCAB.diet_last_six_month, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean};{text}'))

slots.weight_loss_3_month = Slot(uri=MIXS['0000295'], name="weight_loss_3_month", curie=MIXS.curie('0000295'),
                   model_uri=MIXS.VOCAB.weight_loss_3_month, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean};{float} {unit}'))

slots.ihmc_ethnicity = Slot(uri=MIXS['0000895'], name="ihmc_ethnicity", curie=MIXS.curie('0000895'),
                   model_uri=MIXS.VOCAB.ihmc_ethnicity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}|{text}'))

slots.host_occupation = Slot(uri=MIXS['0000896'], name="host_occupation", curie=MIXS.curie('0000896'),
                   model_uri=MIXS.VOCAB.host_occupation, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer}'))

slots.pet_farm_animal = Slot(uri=MIXS['0000267'], name="pet_farm_animal", curie=MIXS.curie('0000267'),
                   model_uri=MIXS.VOCAB.pet_farm_animal, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean};{text}'))

slots.travel_out_six_month = Slot(uri=MIXS['0000268'], name="travel_out_six_month", curie=MIXS.curie('0000268'),
                   model_uri=MIXS.VOCAB.travel_out_six_month, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.twin_sibling = Slot(uri=MIXS['0000326'], name="twin_sibling", curie=MIXS.curie('0000326'),
                   model_uri=MIXS.VOCAB.twin_sibling, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean}'))

slots.medic_hist_perform = Slot(uri=MIXS['0000897'], name="medic_hist_perform", curie=MIXS.curie('0000897'),
                   model_uri=MIXS.VOCAB.medic_hist_perform, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean}'))

slots.study_complt_stat = Slot(uri=MIXS['0000898'], name="study_complt_stat", curie=MIXS.curie('0000898'),
                   model_uri=MIXS.VOCAB.study_complt_stat, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean};[adverse event|non-compliance|lost to follow up|other-specify]'))

slots.pulmonary_disord = Slot(uri=MIXS['0000269'], name="pulmonary_disord", curie=MIXS.curie('0000269'),
                   model_uri=MIXS.VOCAB.pulmonary_disord, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.nose_throat_disord = Slot(uri=MIXS['0000270'], name="nose_throat_disord", curie=MIXS.curie('0000270'),
                   model_uri=MIXS.VOCAB.nose_throat_disord, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.blood_blood_disord = Slot(uri=MIXS['0000271'], name="blood_blood_disord", curie=MIXS.curie('0000271'),
                   model_uri=MIXS.VOCAB.blood_blood_disord, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.host_pulse = Slot(uri=MIXS['0000333'], name="host_pulse", curie=MIXS.curie('0000333'),
                   model_uri=MIXS.VOCAB.host_pulse, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.gestation_state = Slot(uri=MIXS['0000272'], name="gestation_state", curie=MIXS.curie('0000272'),
                   model_uri=MIXS.VOCAB.gestation_state, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.maternal_health_stat = Slot(uri=MIXS['0000273'], name="maternal_health_stat", curie=MIXS.curie('0000273'),
                   model_uri=MIXS.VOCAB.maternal_health_stat, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.foetal_health_stat = Slot(uri=MIXS['0000275'], name="foetal_health_stat", curie=MIXS.curie('0000275'),
                   model_uri=MIXS.VOCAB.foetal_health_stat, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.amniotic_fluid_color = Slot(uri=MIXS['0000276'], name="amniotic_fluid_color", curie=MIXS.curie('0000276'),
                   model_uri=MIXS.VOCAB.amniotic_fluid_color, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.urogenit_tract_disor = Slot(uri=MIXS['0000278'], name="urogenit_tract_disor", curie=MIXS.curie('0000278'),
                   model_uri=MIXS.VOCAB.urogenit_tract_disor, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.urine_collect_meth = Slot(uri=MIXS['0000899'], name="urine_collect_meth", curie=MIXS.curie('0000899'),
                   model_uri=MIXS.VOCAB.urine_collect_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'[clean catch|catheter]'))

slots.gastrointest_disord = Slot(uri=MIXS['0000280'], name="gastrointest_disord", curie=MIXS.curie('0000280'),
                   model_uri=MIXS.VOCAB.gastrointest_disord, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.liver_disord = Slot(uri=MIXS['0000282'], name="liver_disord", curie=MIXS.curie('0000282'),
                   model_uri=MIXS.VOCAB.liver_disord, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.special_diet = Slot(uri=MIXS['0000905'], name="special_diet", curie=MIXS.curie('0000905'),
                   model_uri=MIXS.VOCAB.special_diet, domain=None, range=Optional[str],
                   pattern=re.compile(r'[low carb|reduced calorie|vegetarian|other(to be specified)]'))

slots.nose_mouth_teeth_throat_disord = Slot(uri=MIXS['0000283'], name="nose_mouth_teeth_throat_disord", curie=MIXS.curie('0000283'),
                   model_uri=MIXS.VOCAB.nose_mouth_teeth_throat_disord, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.time_last_toothbrush = Slot(uri=MIXS['0000924'], name="time_last_toothbrush", curie=MIXS.curie('0000924'),
                   model_uri=MIXS.VOCAB.time_last_toothbrush, domain=None, range=Optional[str],
                   pattern=re.compile(r'{duration}'))

slots.dermatology_disord = Slot(uri=MIXS['0000284'], name="dermatology_disord", curie=MIXS.curie('0000284'),
                   model_uri=MIXS.VOCAB.dermatology_disord, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.time_since_last_wash = Slot(uri=MIXS['0000943'], name="time_since_last_wash", curie=MIXS.curie('0000943'),
                   model_uri=MIXS.VOCAB.time_since_last_wash, domain=None, range=Optional[str],
                   pattern=re.compile(r'{duration}'))

slots.dominant_hand = Slot(uri=MIXS['0000944'], name="dominant_hand", curie=MIXS.curie('0000944'),
                   model_uri=MIXS.VOCAB.dominant_hand, domain=None, range=Optional[str],
                   pattern=re.compile(r'[left|right|ambidextrous]'))

slots.menarche = Slot(uri=MIXS['0000965'], name="menarche", curie=MIXS.curie('0000965'),
                   model_uri=MIXS.VOCAB.menarche, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.sexual_act = Slot(uri=MIXS['0000285'], name="sexual_act", curie=MIXS.curie('0000285'),
                   model_uri=MIXS.VOCAB.sexual_act, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.pregnancy = Slot(uri=MIXS['0000966'], name="pregnancy", curie=MIXS.curie('0000966'),
                   model_uri=MIXS.VOCAB.pregnancy, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.douche = Slot(uri=MIXS['0000967'], name="douche", curie=MIXS.curie('0000967'),
                   model_uri=MIXS.VOCAB.douche, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.birth_control = Slot(uri=MIXS['0000286'], name="birth_control", curie=MIXS.curie('0000286'),
                   model_uri=MIXS.VOCAB.birth_control, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.menopause = Slot(uri=MIXS['0000968'], name="menopause", curie=MIXS.curie('0000968'),
                   model_uri=MIXS.VOCAB.menopause, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.hrt = Slot(uri=MIXS['0000969'], name="hrt", curie=MIXS.curie('0000969'),
                   model_uri=MIXS.VOCAB.hrt, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.hysterectomy = Slot(uri=MIXS['0000287'], name="hysterectomy", curie=MIXS.curie('0000287'),
                   model_uri=MIXS.VOCAB.hysterectomy, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean}'))

slots.gynecologic_disord = Slot(uri=MIXS['0000288'], name="gynecologic_disord", curie=MIXS.curie('0000288'),
                   model_uri=MIXS.VOCAB.gynecologic_disord, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.urogenit_disord = Slot(uri=MIXS['0000289'], name="urogenit_disord", curie=MIXS.curie('0000289'),
                   model_uri=MIXS.VOCAB.urogenit_disord, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.hcr = Slot(uri=MIXS['0000988'], name="hcr", curie=MIXS.curie('0000988'),
                   model_uri=MIXS.VOCAB.hcr, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Oil Reservoir|Gas Reservoir|Oil Sand|Coalbed|Shale|Tight Oil Reservoir|Tight Gas Reservoir|other]'))

slots.hc_produced = Slot(uri=MIXS['0000989'], name="hc_produced", curie=MIXS.curie('0000989'),
                   model_uri=MIXS.VOCAB.hc_produced, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Oil|Gas-Condensate|Gas|Bitumen|Coalbed Methane|other]'))

slots.basin = Slot(uri=MIXS['0000290'], name="basin", curie=MIXS.curie('0000290'),
                   model_uri=MIXS.VOCAB.basin, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.field = Slot(uri=MIXS['0000291'], name="field", curie=MIXS.curie('0000291'),
                   model_uri=MIXS.VOCAB.field, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.reservoir = Slot(uri=MIXS['0000303'], name="reservoir", curie=MIXS.curie('0000303'),
                   model_uri=MIXS.VOCAB.reservoir, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.hcr_temp = Slot(uri=MIXS['0000393'], name="hcr_temp", curie=MIXS.curie('0000393'),
                   model_uri=MIXS.VOCAB.hcr_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} - {float} {unit}'))

slots.tvdss_of_hcr_temp = Slot(uri=MIXS['0000394'], name="tvdss_of_hcr_temp", curie=MIXS.curie('0000394'),
                   model_uri=MIXS.VOCAB.tvdss_of_hcr_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.hcr_pressure = Slot(uri=MIXS['0000395'], name="hcr_pressure", curie=MIXS.curie('0000395'),
                   model_uri=MIXS.VOCAB.hcr_pressure, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} - {float} {unit}'))

slots.tvdss_of_hcr_pressure = Slot(uri=MIXS['0000397'], name="tvdss_of_hcr_pressure", curie=MIXS.curie('0000397'),
                   model_uri=MIXS.VOCAB.tvdss_of_hcr_pressure, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.permeability = Slot(uri=MIXS['0000404'], name="permeability", curie=MIXS.curie('0000404'),
                   model_uri=MIXS.VOCAB.permeability, domain=None, range=Optional[str],
                   pattern=re.compile(r'{integer} - {integer} {unit}'))

slots.porosity = Slot(uri=MIXS['0000211'], name="porosity", curie=MIXS.curie('0000211'),
                   model_uri=MIXS.VOCAB.porosity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} - {float} {unit}'))

slots.lithology = Slot(uri=MIXS['0000990'], name="lithology", curie=MIXS.curie('0000990'),
                   model_uri=MIXS.VOCAB.lithology, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Basement|Chalk|Chert|Coal|Conglomerate|Diatomite|Dolomite|Limestone|Sandstone|Shale|Siltstone|Volcanic|other]'))

slots.depos_env = Slot(uri=MIXS['0000992'], name="depos_env", curie=MIXS.curie('0000992'),
                   model_uri=MIXS.VOCAB.depos_env, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Continental - Alluvial|Continental - Aeolian|Continental - Fluvial|Continental - Lacustrine|Transitional - Deltaic|Transitional - Tidal|Transitional - Lagoonal|Transitional - Beach|Transitional - Lake|Marine - Shallow|Marine - Deep|Marine - Reef|Other - Evaporite|Other - Glacial|Other - Volcanic|other]'))

slots.hcr_geol_age = Slot(uri=MIXS['0000993'], name="hcr_geol_age", curie=MIXS.curie('0000993'),
                   model_uri=MIXS.VOCAB.hcr_geol_age, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Archean|Cambrian|Carboniferous|Cenozoic|Cretaceous|Devonian|Jurassic|Mesozoic|Neogene|Ordovician|Paleogene|Paleozoic|Permian|Precambrian|Proterozoic|Silurian|Triassic|other]'))

slots.owc_tvdss = Slot(uri=MIXS['0000405'], name="owc_tvdss", curie=MIXS.curie('0000405'),
                   model_uri=MIXS.VOCAB.owc_tvdss, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.hcr_fw_salinity = Slot(uri=MIXS['0000406'], name="hcr_fw_salinity", curie=MIXS.curie('0000406'),
                   model_uri=MIXS.VOCAB.hcr_fw_salinity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.sulfate_fw = Slot(uri=MIXS['0000407'], name="sulfate_fw", curie=MIXS.curie('0000407'),
                   model_uri=MIXS.VOCAB.sulfate_fw, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.vfa_fw = Slot(uri=MIXS['0000408'], name="vfa_fw", curie=MIXS.curie('0000408'),
                   model_uri=MIXS.VOCAB.vfa_fw, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.sr_kerog_type = Slot(uri=MIXS['0000994'], name="sr_kerog_type", curie=MIXS.curie('0000994'),
                   model_uri=MIXS.VOCAB.sr_kerog_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Type I|Type II|Type III|Type IV|other]'))

slots.sr_lithology = Slot(uri=MIXS['0000995'], name="sr_lithology", curie=MIXS.curie('0000995'),
                   model_uri=MIXS.VOCAB.sr_lithology, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Clastic|Carbonate|Coal|Biosilicieous|other]'))

slots.sr_dep_env = Slot(uri=MIXS['0000996'], name="sr_dep_env", curie=MIXS.curie('0000996'),
                   model_uri=MIXS.VOCAB.sr_dep_env, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Lacustine|Fluvioldeltaic|Fluviomarine|Marine|other]'))

slots.sr_geol_age = Slot(uri=MIXS['0000997'], name="sr_geol_age", curie=MIXS.curie('0000997'),
                   model_uri=MIXS.VOCAB.sr_geol_age, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Archean|Cambrian|Carboniferous|Cenozoic|Cretaceous|Devonian|Jurassic|Mesozoic|Neogene|Ordovician|Paleogene|Paleozoic|Permian|Precambrian|Proterozoic|Silurian|Triassic|other]'))

slots.samp_well_name = Slot(uri=MIXS['0000296'], name="samp_well_name", curie=MIXS.curie('0000296'),
                   model_uri=MIXS.VOCAB.samp_well_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.win = Slot(uri=MIXS['0000297'], name="win", curie=MIXS.curie('0000297'),
                   model_uri=MIXS.VOCAB.win, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.samp_type = Slot(uri=MIXS['0000998'], name="samp_type", curie=MIXS.curie('0000998'),
                   model_uri=MIXS.VOCAB.samp_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[core|rock trimmings|drill cuttings|piping section|coupon|pigging debris|solid deposit|produced fluid|produced water|injected water|water from treatment plant|fresh water|sea water|drilling fluid|procedural blank|positive control|negative control|other]'))

slots.samp_subtype = Slot(uri=MIXS['0000999'], name="samp_subtype", curie=MIXS.curie('0000999'),
                   model_uri=MIXS.VOCAB.samp_subtype, domain=None, range=Optional[str],
                   pattern=re.compile(r'[oil phase|water phase|biofilm|not applicable|other]'))

slots.pressure = Slot(uri=MIXS['0000412'], name="pressure", curie=MIXS.curie('0000412'),
                   model_uri=MIXS.VOCAB.pressure, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.samp_tvdss = Slot(uri=MIXS['0000409'], name="samp_tvdss", curie=MIXS.curie('0000409'),
                   model_uri=MIXS.VOCAB.samp_tvdss, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float}-{float} {unit}'))

slots.samp_md = Slot(uri=MIXS['0000413'], name="samp_md", curie=MIXS.curie('0000413'),
                   model_uri=MIXS.VOCAB.samp_md, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};[GL|DF|RT|KB|MSL|other]'))

slots.samp_transport_cond = Slot(uri=MIXS['0000410'], name="samp_transport_cond", curie=MIXS.curie('0000410'),
                   model_uri=MIXS.VOCAB.samp_transport_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};{float} {unit}'))

slots.organism_count_qpcr_info = Slot(uri=MIXS['0000099'], name="organism_count_qpcr_info", curie=MIXS.curie('0000099'),
                   model_uri=MIXS.VOCAB.organism_count_qpcr_info, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};FWD:{dna};REV:{dna};initial denaturation:degrees_minutes;denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final elongation:degrees_minutes; total cycles'))

slots.ph = Slot(uri=MIXS['0001001'], name="ph", curie=MIXS.curie('0001001'),
                   model_uri=MIXS.VOCAB.ph, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float}'))

slots.alkalinity = Slot(uri=MIXS['0000421'], name="alkalinity", curie=MIXS.curie('0000421'),
                   model_uri=MIXS.VOCAB.alkalinity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.alkalinity_method = Slot(uri=MIXS['0000298'], name="alkalinity_method", curie=MIXS.curie('0000298'),
                   model_uri=MIXS.VOCAB.alkalinity_method, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.sulfate = Slot(uri=MIXS['0000423'], name="sulfate", curie=MIXS.curie('0000423'),
                   model_uri=MIXS.VOCAB.sulfate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.sulfide = Slot(uri=MIXS['0000424'], name="sulfide", curie=MIXS.curie('0000424'),
                   model_uri=MIXS.VOCAB.sulfide, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tot_sulfur = Slot(uri=MIXS['0000419'], name="tot_sulfur", curie=MIXS.curie('0000419'),
                   model_uri=MIXS.VOCAB.tot_sulfur, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.nitrate = Slot(uri=MIXS['0000425'], name="nitrate", curie=MIXS.curie('0000425'),
                   model_uri=MIXS.VOCAB.nitrate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.nitrite = Slot(uri=MIXS['0000426'], name="nitrite", curie=MIXS.curie('0000426'),
                   model_uri=MIXS.VOCAB.nitrite, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.ammonium = Slot(uri=MIXS['0000427'], name="ammonium", curie=MIXS.curie('0000427'),
                   model_uri=MIXS.VOCAB.ammonium, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tot_nitro = Slot(uri=MIXS['0000102'], name="tot_nitro", curie=MIXS.curie('0000102'),
                   model_uri=MIXS.VOCAB.tot_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diss_iron = Slot(uri=MIXS['0000139'], name="diss_iron", curie=MIXS.curie('0000139'),
                   model_uri=MIXS.VOCAB.diss_iron, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.sodium = Slot(uri=MIXS['0000428'], name="sodium", curie=MIXS.curie('0000428'),
                   model_uri=MIXS.VOCAB.sodium, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.chloride = Slot(uri=MIXS['0000429'], name="chloride", curie=MIXS.curie('0000429'),
                   model_uri=MIXS.VOCAB.chloride, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.potassium = Slot(uri=MIXS['0000430'], name="potassium", curie=MIXS.curie('0000430'),
                   model_uri=MIXS.VOCAB.potassium, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.magnesium = Slot(uri=MIXS['0000431'], name="magnesium", curie=MIXS.curie('0000431'),
                   model_uri=MIXS.VOCAB.magnesium, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.calcium = Slot(uri=MIXS['0000432'], name="calcium", curie=MIXS.curie('0000432'),
                   model_uri=MIXS.VOCAB.calcium, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tot_iron = Slot(uri=MIXS['0000105'], name="tot_iron", curie=MIXS.curie('0000105'),
                   model_uri=MIXS.VOCAB.tot_iron, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diss_org_carb = Slot(uri=MIXS['0000433'], name="diss_org_carb", curie=MIXS.curie('0000433'),
                   model_uri=MIXS.VOCAB.diss_org_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diss_inorg_carb = Slot(uri=MIXS['0000434'], name="diss_inorg_carb", curie=MIXS.curie('0000434'),
                   model_uri=MIXS.VOCAB.diss_inorg_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diss_inorg_phosp = Slot(uri=MIXS['0000106'], name="diss_inorg_phosp", curie=MIXS.curie('0000106'),
                   model_uri=MIXS.VOCAB.diss_inorg_phosp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tot_phosp = Slot(uri=MIXS['0000117'], name="tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=MIXS.VOCAB.tot_phosp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.suspend_solids = Slot(uri=MIXS['0000150'], name="suspend_solids", curie=MIXS.curie('0000150'),
                   model_uri=MIXS.VOCAB.suspend_solids, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.density = Slot(uri=MIXS['0000435'], name="density", curie=MIXS.curie('0000435'),
                   model_uri=MIXS.VOCAB.density, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diss_carb_dioxide = Slot(uri=MIXS['0000436'], name="diss_carb_dioxide", curie=MIXS.curie('0000436'),
                   model_uri=MIXS.VOCAB.diss_carb_dioxide, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diss_oxygen_fluid = Slot(uri=MIXS['0000438'], name="diss_oxygen_fluid", curie=MIXS.curie('0000438'),
                   model_uri=MIXS.VOCAB.diss_oxygen_fluid, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.vfa = Slot(uri=MIXS['0000152'], name="vfa", curie=MIXS.curie('0000152'),
                   model_uri=MIXS.VOCAB.vfa, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.benzene = Slot(uri=MIXS['0000153'], name="benzene", curie=MIXS.curie('0000153'),
                   model_uri=MIXS.VOCAB.benzene, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.toluene = Slot(uri=MIXS['0000154'], name="toluene", curie=MIXS.curie('0000154'),
                   model_uri=MIXS.VOCAB.toluene, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.ethylbenzene = Slot(uri=MIXS['0000155'], name="ethylbenzene", curie=MIXS.curie('0000155'),
                   model_uri=MIXS.VOCAB.ethylbenzene, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.xylene = Slot(uri=MIXS['0000156'], name="xylene", curie=MIXS.curie('0000156'),
                   model_uri=MIXS.VOCAB.xylene, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.api = Slot(uri=MIXS['0000157'], name="api", curie=MIXS.curie('0000157'),
                   model_uri=MIXS.VOCAB.api, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tan = Slot(uri=MIXS['0000120'], name="tan", curie=MIXS.curie('0000120'),
                   model_uri=MIXS.VOCAB.tan, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.viscosity = Slot(uri=MIXS['0000126'], name="viscosity", curie=MIXS.curie('0000126'),
                   model_uri=MIXS.VOCAB.viscosity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};{float} {unit}'))

slots.pour_point = Slot(uri=MIXS['0000127'], name="pour_point", curie=MIXS.curie('0000127'),
                   model_uri=MIXS.VOCAB.pour_point, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.saturates_pc = Slot(uri=MIXS['0000131'], name="saturates_pc", curie=MIXS.curie('0000131'),
                   model_uri=MIXS.VOCAB.saturates_pc, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.aromatics_pc = Slot(uri=MIXS['0000133'], name="aromatics_pc", curie=MIXS.curie('0000133'),
                   model_uri=MIXS.VOCAB.aromatics_pc, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.resins_pc = Slot(uri=MIXS['0000134'], name="resins_pc", curie=MIXS.curie('0000134'),
                   model_uri=MIXS.VOCAB.resins_pc, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.asphaltenes_pc = Slot(uri=MIXS['0000135'], name="asphaltenes_pc", curie=MIXS.curie('0000135'),
                   model_uri=MIXS.VOCAB.asphaltenes_pc, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.additional_info = Slot(uri=MIXS['0000300'], name="additional_info", curie=MIXS.curie('0000300'),
                   model_uri=MIXS.VOCAB.additional_info, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.prod_start_date = Slot(uri=MIXS['0001008'], name="prod_start_date", curie=MIXS.curie('0001008'),
                   model_uri=MIXS.VOCAB.prod_start_date, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.prod_rate = Slot(uri=MIXS['0000452'], name="prod_rate", curie=MIXS.curie('0000452'),
                   model_uri=MIXS.VOCAB.prod_rate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.water_production_rate = Slot(uri=MIXS['0000453'], name="water_production_rate", curie=MIXS.curie('0000453'),
                   model_uri=MIXS.VOCAB.water_production_rate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.water_cut = Slot(uri=MIXS['0000454'], name="water_cut", curie=MIXS.curie('0000454'),
                   model_uri=MIXS.VOCAB.water_cut, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.iwf = Slot(uri=MIXS['0000455'], name="iwf", curie=MIXS.curie('0000455'),
                   model_uri=MIXS.VOCAB.iwf, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.add_recov_method = Slot(uri=MIXS['0001009'], name="add_recov_method", curie=MIXS.curie('0001009'),
                   model_uri=MIXS.VOCAB.add_recov_method, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Water Injection|Dump Flood|Gas Injection|Wag Immiscible Injection|Polymer Addition|Surfactant Addition|Not Applicable|other];{timestamp}'))

slots.iw_bt_date_well = Slot(uri=MIXS['0001010'], name="iw_bt_date_well", curie=MIXS.curie('0001010'),
                   model_uri=MIXS.VOCAB.iw_bt_date_well, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.biocide = Slot(uri=MIXS['0001011'], name="biocide", curie=MIXS.curie('0001011'),
                   model_uri=MIXS.VOCAB.biocide, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{text};{timestamp}'))

slots.biocide_admin_method = Slot(uri=MIXS['0000456'], name="biocide_admin_method", curie=MIXS.curie('0000456'),
                   model_uri=MIXS.VOCAB.biocide_admin_method, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};{Rn/start_time/end_time/duration};{duration}'))

slots.chem_treatment = Slot(uri=MIXS['0001012'], name="chem_treatment", curie=MIXS.curie('0001012'),
                   model_uri=MIXS.VOCAB.chem_treatment, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{text};{timestamp}'))

slots.chem_treatment_method = Slot(uri=MIXS['0000457'], name="chem_treatment_method", curie=MIXS.curie('0000457'),
                   model_uri=MIXS.VOCAB.chem_treatment_method, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};{Rn/start_time/end_time/duration};{duration};{duration}'))

slots.samp_loc_corr_rate = Slot(uri=MIXS['0000136'], name="samp_loc_corr_rate", curie=MIXS.curie('0000136'),
                   model_uri=MIXS.VOCAB.samp_loc_corr_rate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} - {float} {unit}'))

slots.samp_collection_point = Slot(uri=MIXS['0001015'], name="samp_collection_point", curie=MIXS.curie('0001015'),
                   model_uri=MIXS.VOCAB.samp_collection_point, domain=None, range=Optional[str],
                   pattern=re.compile(r'[well|test well|drilling rig|wellhead|separator|storage tank|other]'))

slots.samp_preserv = Slot(uri=MIXS['0000463'], name="samp_preserv", curie=MIXS.curie('0000463'),
                   model_uri=MIXS.VOCAB.samp_preserv, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.alkyl_diethers = Slot(uri=MIXS['0000490'], name="alkyl_diethers", curie=MIXS.curie('0000490'),
                   model_uri=MIXS.VOCAB.alkyl_diethers, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.aminopept_act = Slot(uri=MIXS['0000172'], name="aminopept_act", curie=MIXS.curie('0000172'),
                   model_uri=MIXS.VOCAB.aminopept_act, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.bacteria_carb_prod = Slot(uri=MIXS['0000173'], name="bacteria_carb_prod", curie=MIXS.curie('0000173'),
                   model_uri=MIXS.VOCAB.bacteria_carb_prod, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.biomass = Slot(uri=MIXS['0000174'], name="biomass", curie=MIXS.curie('0000174'),
                   model_uri=MIXS.VOCAB.biomass, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.bishomohopanol = Slot(uri=MIXS['0000175'], name="bishomohopanol", curie=MIXS.curie('0000175'),
                   model_uri=MIXS.VOCAB.bishomohopanol, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.bromide = Slot(uri=MIXS['0000176'], name="bromide", curie=MIXS.curie('0000176'),
                   model_uri=MIXS.VOCAB.bromide, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=MIXS.VOCAB.carb_nitro_ratio, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.chlorophyll = Slot(uri=MIXS['0000177'], name="chlorophyll", curie=MIXS.curie('0000177'),
                   model_uri=MIXS.VOCAB.chlorophyll, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diether_lipids = Slot(uri=MIXS['0000178'], name="diether_lipids", curie=MIXS.curie('0000178'),
                   model_uri=MIXS.VOCAB.diether_lipids, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.diss_hydrogen = Slot(uri=MIXS['0000179'], name="diss_hydrogen", curie=MIXS.curie('0000179'),
                   model_uri=MIXS.VOCAB.diss_hydrogen, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diss_org_nitro = Slot(uri=MIXS['0000162'], name="diss_org_nitro", curie=MIXS.curie('0000162'),
                   model_uri=MIXS.VOCAB.diss_org_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diss_oxygen = Slot(uri=MIXS['0000119'], name="diss_oxygen", curie=MIXS.curie('0000119'),
                   model_uri=MIXS.VOCAB.diss_oxygen, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.glucosidase_act = Slot(uri=MIXS['0000137'], name="glucosidase_act", curie=MIXS.curie('0000137'),
                   model_uri=MIXS.VOCAB.glucosidase_act, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.mean_frict_vel = Slot(uri=MIXS['0000498'], name="mean_frict_vel", curie=MIXS.curie('0000498'),
                   model_uri=MIXS.VOCAB.mean_frict_vel, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.mean_peak_frict_vel = Slot(uri=MIXS['0000502'], name="mean_peak_frict_vel", curie=MIXS.curie('0000502'),
                   model_uri=MIXS.VOCAB.mean_peak_frict_vel, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.n_alkanes = Slot(uri=MIXS['0000503'], name="n_alkanes", curie=MIXS.curie('0000503'),
                   model_uri=MIXS.VOCAB.n_alkanes, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.nitro = Slot(uri=MIXS['0000504'], name="nitro", curie=MIXS.curie('0000504'),
                   model_uri=MIXS.VOCAB.nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.org_carb = Slot(uri=MIXS['0000508'], name="org_carb", curie=MIXS.curie('0000508'),
                   model_uri=MIXS.VOCAB.org_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.org_matter = Slot(uri=MIXS['0000204'], name="org_matter", curie=MIXS.curie('0000204'),
                   model_uri=MIXS.VOCAB.org_matter, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.org_nitro = Slot(uri=MIXS['0000205'], name="org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=MIXS.VOCAB.org_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.part_org_carb = Slot(uri=MIXS['0000515'], name="part_org_carb", curie=MIXS.curie('0000515'),
                   model_uri=MIXS.VOCAB.part_org_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.petroleum_hydrocarb = Slot(uri=MIXS['0000516'], name="petroleum_hydrocarb", curie=MIXS.curie('0000516'),
                   model_uri=MIXS.VOCAB.petroleum_hydrocarb, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.phaeopigments = Slot(uri=MIXS['0000180'], name="phaeopigments", curie=MIXS.curie('0000180'),
                   model_uri=MIXS.VOCAB.phaeopigments, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.phosphate = Slot(uri=MIXS['0000505'], name="phosphate", curie=MIXS.curie('0000505'),
                   model_uri=MIXS.VOCAB.phosphate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.phosplipid_fatt_acid = Slot(uri=MIXS['0000181'], name="phosplipid_fatt_acid", curie=MIXS.curie('0000181'),
                   model_uri=MIXS.VOCAB.phosplipid_fatt_acid, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.redox_potential = Slot(uri=MIXS['0000182'], name="redox_potential", curie=MIXS.curie('0000182'),
                   model_uri=MIXS.VOCAB.redox_potential, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.salinity = Slot(uri=MIXS['0000183'], name="salinity", curie=MIXS.curie('0000183'),
                   model_uri=MIXS.VOCAB.salinity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.silicate = Slot(uri=MIXS['0000184'], name="silicate", curie=MIXS.curie('0000184'),
                   model_uri=MIXS.VOCAB.silicate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tot_carb = Slot(uri=MIXS['0000525'], name="tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=MIXS.VOCAB.tot_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tot_nitro_content = Slot(uri=MIXS['0000530'], name="tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=MIXS.VOCAB.tot_nitro_content, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tot_org_carb = Slot(uri=MIXS['0000533'], name="tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=MIXS.VOCAB.tot_org_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.turbidity = Slot(uri=MIXS['0000191'], name="turbidity", curie=MIXS.curie('0000191'),
                   model_uri=MIXS.VOCAB.turbidity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.water_content = Slot(uri=MIXS['0000185'], name="water_content", curie=MIXS.curie('0000185'),
                   model_uri=MIXS.VOCAB.water_content, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.water_current = Slot(uri=MIXS['0000203'], name="water_current", curie=MIXS.curie('0000203'),
                   model_uri=MIXS.VOCAB.water_current, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.air_temp_regm = Slot(uri=MIXS['0000551'], name="air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=MIXS.VOCAB.air_temp_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};{Rn/start_time/end_time/duration}'))

slots.antibiotic_regm = Slot(uri=MIXS['0000553'], name="antibiotic_regm", curie=MIXS.curie('0000553'),
                   model_uri=MIXS.VOCAB.antibiotic_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.biotic_regm = Slot(uri=MIXS['0001038'], name="biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=MIXS.VOCAB.biotic_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.chem_mutagen = Slot(uri=MIXS['0000555'], name="chem_mutagen", curie=MIXS.curie('0000555'),
                   model_uri=MIXS.VOCAB.chem_mutagen, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.climate_environment = Slot(uri=MIXS['0001040'], name="climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=MIXS.VOCAB.climate_environment, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{Rn/start_time/end_time/duration}'))

slots.cult_root_med = Slot(uri=MIXS['0001041'], name="cult_root_med", curie=MIXS.curie('0001041'),
                   model_uri=MIXS.VOCAB.cult_root_med, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}|{PMID}|{DOI}|{URL}'))

slots.fertilizer_regm = Slot(uri=MIXS['0000556'], name="fertilizer_regm", curie=MIXS.curie('0000556'),
                   model_uri=MIXS.VOCAB.fertilizer_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.fungicide_regm = Slot(uri=MIXS['0000557'], name="fungicide_regm", curie=MIXS.curie('0000557'),
                   model_uri=MIXS.VOCAB.fungicide_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.gaseous_environment = Slot(uri=MIXS['0000558'], name="gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=MIXS.VOCAB.gaseous_environment, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.gravity = Slot(uri=MIXS['0000559'], name="gravity", curie=MIXS.curie('0000559'),
                   model_uri=MIXS.VOCAB.gravity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};{Rn/start_time/end_time/duration}'))

slots.growth_facil = Slot(uri=MIXS['0001043'], name="growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=MIXS.VOCAB.growth_facil, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}|{termLabel} {[termID]}'))

slots.growth_habit = Slot(uri=MIXS['0001044'], name="growth_habit", curie=MIXS.curie('0001044'),
                   model_uri=MIXS.VOCAB.growth_habit, domain=None, range=Optional[str],
                   pattern=re.compile(r'[erect|semi-erect|spreading|prostrate]'))

slots.growth_hormone_regm = Slot(uri=MIXS['0000560'], name="growth_hormone_regm", curie=MIXS.curie('0000560'),
                   model_uri=MIXS.VOCAB.growth_hormone_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.herbicide_regm = Slot(uri=MIXS['0000561'], name="herbicide_regm", curie=MIXS.curie('0000561'),
                   model_uri=MIXS.VOCAB.herbicide_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.host_wet_mass = Slot(uri=MIXS['0000567'], name="host_wet_mass", curie=MIXS.curie('0000567'),
                   model_uri=MIXS.VOCAB.host_wet_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.humidity_regm = Slot(uri=MIXS['0000568'], name="humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=MIXS.VOCAB.humidity_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};{Rn/start_time/end_time/duration}'))

slots.light_regm = Slot(uri=MIXS['0000569'], name="light_regm", curie=MIXS.curie('0000569'),
                   model_uri=MIXS.VOCAB.light_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{float} {unit}'))

slots.mechanical_damage = Slot(uri=MIXS['0001052'], name="mechanical_damage", curie=MIXS.curie('0001052'),
                   model_uri=MIXS.VOCAB.mechanical_damage, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{text}'))

slots.mineral_nutr_regm = Slot(uri=MIXS['0000570'], name="mineral_nutr_regm", curie=MIXS.curie('0000570'),
                   model_uri=MIXS.VOCAB.mineral_nutr_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.non_mineral_nutr_regm = Slot(uri=MIXS['0000571'], name="non_mineral_nutr_regm", curie=MIXS.curie('0000571'),
                   model_uri=MIXS.VOCAB.non_mineral_nutr_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.ph_regm = Slot(uri=MIXS['0001056'], name="ph_regm", curie=MIXS.curie('0001056'),
                   model_uri=MIXS.VOCAB.ph_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float};{Rn/start_time/end_time/duration}'))

slots.pesticide_regm = Slot(uri=MIXS['0000573'], name="pesticide_regm", curie=MIXS.curie('0000573'),
                   model_uri=MIXS.VOCAB.pesticide_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.plant_growth_med = Slot(uri=MIXS['0001057'], name="plant_growth_med", curie=MIXS.curie('0001057'),
                   model_uri=MIXS.VOCAB.plant_growth_med, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]} or [husk|other artificial liquid medium|other artificial solid medium|peat moss|perlite|pumice|sand|soil|vermiculite|water]'))

slots.plant_product = Slot(uri=MIXS['0001058'], name="plant_product", curie=MIXS.curie('0001058'),
                   model_uri=MIXS.VOCAB.plant_product, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.plant_sex = Slot(uri=MIXS['0001059'], name="plant_sex", curie=MIXS.curie('0001059'),
                   model_uri=MIXS.VOCAB.plant_sex, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Androdioecious|Androecious|Androgynous|Androgynomonoecious|Andromonoecious|Bisexual|Dichogamous|Diclinous|Dioecious|Gynodioecious|Gynoecious|Gynomonoecious|Hermaphroditic|Imperfect|Monoclinous|Monoecious|Perfect|Polygamodioecious|Polygamomonoecious|Polygamous|Protandrous|Protogynous|Subandroecious|Subdioecious|Subgynoecious|Synoecious|Trimonoecious|Trioecious|Unisexual]'))

slots.plant_struc = Slot(uri=MIXS['0001060'], name="plant_struc", curie=MIXS.curie('0001060'),
                   model_uri=MIXS.VOCAB.plant_struc, domain=None, range=Optional[str],
                   pattern=re.compile(r'{termLabel} {[termID]}'))

slots.radiation_regm = Slot(uri=MIXS['0000575'], name="radiation_regm", curie=MIXS.curie('0000575'),
                   model_uri=MIXS.VOCAB.radiation_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.rainfall_regm = Slot(uri=MIXS['0000576'], name="rainfall_regm", curie=MIXS.curie('0000576'),
                   model_uri=MIXS.VOCAB.rainfall_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};{Rn/start_time/end_time/duration}'))

slots.root_cond = Slot(uri=MIXS['0001061'], name="root_cond", curie=MIXS.curie('0001061'),
                   model_uri=MIXS.VOCAB.root_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}|{text}'))

slots.root_med_carbon = Slot(uri=MIXS['0000577'], name="root_med_carbon", curie=MIXS.curie('0000577'),
                   model_uri=MIXS.VOCAB.root_med_carbon, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.root_med_macronutr = Slot(uri=MIXS['0000578'], name="root_med_macronutr", curie=MIXS.curie('0000578'),
                   model_uri=MIXS.VOCAB.root_med_macronutr, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.root_med_micronutr = Slot(uri=MIXS['0000579'], name="root_med_micronutr", curie=MIXS.curie('0000579'),
                   model_uri=MIXS.VOCAB.root_med_micronutr, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.root_med_suppl = Slot(uri=MIXS['0000580'], name="root_med_suppl", curie=MIXS.curie('0000580'),
                   model_uri=MIXS.VOCAB.root_med_suppl, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.root_med_ph = Slot(uri=MIXS['0001062'], name="root_med_ph", curie=MIXS.curie('0001062'),
                   model_uri=MIXS.VOCAB.root_med_ph, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float}'))

slots.root_med_regl = Slot(uri=MIXS['0000581'], name="root_med_regl", curie=MIXS.curie('0000581'),
                   model_uri=MIXS.VOCAB.root_med_regl, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.root_med_solid = Slot(uri=MIXS['0001063'], name="root_med_solid", curie=MIXS.curie('0001063'),
                   model_uri=MIXS.VOCAB.root_med_solid, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.salt_regm = Slot(uri=MIXS['0000582'], name="salt_regm", curie=MIXS.curie('0000582'),
                   model_uri=MIXS.VOCAB.salt_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{Rn/start_time/end_time/duration}'))

slots.season_environment = Slot(uri=MIXS['0001068'], name="season_environment", curie=MIXS.curie('0001068'),
                   model_uri=MIXS.VOCAB.season_environment, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{Rn/start_time/end_time/duration}'))

slots.standing_water_regm = Slot(uri=MIXS['0001069'], name="standing_water_regm", curie=MIXS.curie('0001069'),
                   model_uri=MIXS.VOCAB.standing_water_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{Rn/start_time/end_time/duration}'))

slots.tiss_cult_growth_med = Slot(uri=MIXS['0001070'], name="tiss_cult_growth_med", curie=MIXS.curie('0001070'),
                   model_uri=MIXS.VOCAB.tiss_cult_growth_med, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}|{text}'))

slots.water_temp_regm = Slot(uri=MIXS['0000590'], name="water_temp_regm", curie=MIXS.curie('0000590'),
                   model_uri=MIXS.VOCAB.water_temp_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};{Rn/start_time/end_time/duration}'))

slots.watering_regm = Slot(uri=MIXS['0000591'], name="watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=MIXS.VOCAB.watering_regm, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit};{Rn/start_time/end_time/duration}'))

slots.particle_class = Slot(uri=MIXS['0000206'], name="particle_class", curie=MIXS.curie('0000206'),
                   model_uri=MIXS.VOCAB.particle_class, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.sediment_type = Slot(uri=MIXS['0001078'], name="sediment_type", curie=MIXS.curie('0001078'),
                   model_uri=MIXS.VOCAB.sediment_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'[biogenous|cosmogenous|hydrogenous|lithogenous]'))

slots.tidal_stage = Slot(uri=MIXS['0000750'], name="tidal_stage", curie=MIXS.curie('0000750'),
                   model_uri=MIXS.VOCAB.tidal_stage, domain=None, range=Optional[str],
                   pattern=re.compile(r'[low tide|ebb tide|flood tide|high tide]'))

slots.tot_depth_water_col = Slot(uri=MIXS['0000634'], name="tot_depth_water_col", curie=MIXS.curie('0000634'),
                   model_uri=MIXS.VOCAB.tot_depth_water_col, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.cur_land_use = Slot(uri=MIXS['0001080'], name="cur_land_use", curie=MIXS.curie('0001080'),
                   model_uri=MIXS.VOCAB.cur_land_use, domain=None, range=Optional[str],
                   pattern=re.compile(r'[cities|farmstead|industrial areas|roads/railroads|rock|sand|gravel|mudflats|salt flats|badlands|permanent snow or ice|saline seeps|mines/quarries|oil waste areas|small grains|row crops|vegetable crops|horticultural plants (e.g. tulips)|marshlands (grass,sedges,rushes)|tundra (mosses,lichens)|rangeland|pastureland (grasslands used for livestock grazing)|hayland|meadows (grasses,alfalfa,fescue,bromegrass,timothy)|shrub land (e.g. mesquite,sage-brush,creosote bush,shrub oak,eucalyptus)|successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub dogwoods,blackberries)|shrub crops (blueberries,nursery ornamentals,filberts)|vine crops (grapes)|conifers (e.g. pine,spruce,fir,cypress)|hardwoods (e.g. oak,hickory,elm,aspen)|intermixed hardwood and conifers|tropical (e.g. mangrove,palms)|rainforest (evergreen forest receiving >406 cm annual rainfall)|swamp (permanent or semi-permanent water body dominated by woody plants)|crop trees (nuts,fruit,christmas trees,nursery trees)]'))

slots.cur_vegetation = Slot(uri=MIXS['0000312'], name="cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=MIXS.VOCAB.cur_vegetation, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=MIXS.VOCAB.cur_vegetation_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.previous_land_use = Slot(uri=MIXS['0000315'], name="previous_land_use", curie=MIXS.curie('0000315'),
                   model_uri=MIXS.VOCAB.previous_land_use, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{timestamp}'))

slots.previous_land_use_meth = Slot(uri=MIXS['0000316'], name="previous_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=MIXS.VOCAB.previous_land_use_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.crop_rotation = Slot(uri=MIXS['0000318'], name="crop_rotation", curie=MIXS.curie('0000318'),
                   model_uri=MIXS.VOCAB.crop_rotation, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean};{Rn/start_time/end_time/duration}'))

slots.agrochem_addition = Slot(uri=MIXS['0000639'], name="agrochem_addition", curie=MIXS.curie('0000639'),
                   model_uri=MIXS.VOCAB.agrochem_addition, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit};{timestamp}'))

slots.tillage = Slot(uri=MIXS['0001081'], name="tillage", curie=MIXS.curie('0001081'),
                   model_uri=MIXS.VOCAB.tillage, domain=None, range=Optional[str],
                   pattern=re.compile(r'[drill|cutting disc|ridge till|strip tillage|zonal tillage|chisel|tined|mouldboard|disc plough]'))

slots.fire = Slot(uri=MIXS['0001086'], name="fire", curie=MIXS.curie('0001086'),
                   model_uri=MIXS.VOCAB.fire, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.flooding = Slot(uri=MIXS['0000319'], name="flooding", curie=MIXS.curie('0000319'),
                   model_uri=MIXS.VOCAB.flooding, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.extreme_event = Slot(uri=MIXS['0000320'], name="extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=MIXS.VOCAB.extreme_event, domain=None, range=Optional[str],
                   pattern=re.compile(r'{timestamp}'))

slots.horizon = Slot(uri=MIXS['0001082'], name="horizon", curie=MIXS.curie('0001082'),
                   model_uri=MIXS.VOCAB.horizon, domain=None, range=Optional[str],
                   pattern=re.compile(r'[O horizon|A horizon|E horizon|B horizon|C horizon|R layer|Permafrost]'))

slots.horizon_meth = Slot(uri=MIXS['0000321'], name="horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=MIXS.VOCAB.horizon_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.sieving = Slot(uri=MIXS['0000322'], name="sieving", curie=MIXS.curie('0000322'),
                   model_uri=MIXS.VOCAB.sieving, domain=None, range=Optional[str],
                   pattern=re.compile(r'{{text}|{float} {unit}};{float} {unit}'))

slots.water_content_soil_meth = Slot(uri=MIXS['0000323'], name="water_content_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=MIXS.VOCAB.water_content_soil_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.pool_dna_extracts = Slot(uri=MIXS['0000325'], name="pool_dna_extracts", curie=MIXS.curie('0000325'),
                   model_uri=MIXS.VOCAB.pool_dna_extracts, domain=None, range=Optional[str],
                   pattern=re.compile(r'{boolean};{integer}'))

slots.store_cond = Slot(uri=MIXS['0000327'], name="store_cond", curie=MIXS.curie('0000327'),
                   model_uri=MIXS.VOCAB.store_cond, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{duration}'))

slots.link_climate_info = Slot(uri=MIXS['0000328'], name="link_climate_info", curie=MIXS.curie('0000328'),
                   model_uri=MIXS.VOCAB.link_climate_info, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.annual_temp = Slot(uri=MIXS['0000642'], name="annual_temp", curie=MIXS.curie('0000642'),
                   model_uri=MIXS.VOCAB.annual_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.season_temp = Slot(uri=MIXS['0000643'], name="season_temp", curie=MIXS.curie('0000643'),
                   model_uri=MIXS.VOCAB.season_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.annual_precpt = Slot(uri=MIXS['0000644'], name="annual_precpt", curie=MIXS.curie('0000644'),
                   model_uri=MIXS.VOCAB.annual_precpt, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.season_precpt = Slot(uri=MIXS['0000645'], name="season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=MIXS.VOCAB.season_precpt, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.link_class_info = Slot(uri=MIXS['0000329'], name="link_class_info", curie=MIXS.curie('0000329'),
                   model_uri=MIXS.VOCAB.link_class_info, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.fao_class = Slot(uri=MIXS['0001083'], name="fao_class", curie=MIXS.curie('0001083'),
                   model_uri=MIXS.VOCAB.fao_class, domain=None, range=Optional[str],
                   pattern=re.compile(r'[Acrisols|Andosols|Arenosols|Cambisols|Chernozems|Ferralsols|Fluvisols|Gleysols|Greyzems|Gypsisols|Histosols|Kastanozems|Lithosols|Luvisols|Nitosols|Phaeozems|Planosols|Podzols|Podzoluvisols|Rankers|Regosols|Rendzinas|Solonchaks|Solonetz|Vertisols|Yermosols]'))

slots.local_class = Slot(uri=MIXS['0000330'], name="local_class", curie=MIXS.curie('0000330'),
                   model_uri=MIXS.VOCAB.local_class, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.local_class_meth = Slot(uri=MIXS['0000331'], name="local_class_meth", curie=MIXS.curie('0000331'),
                   model_uri=MIXS.VOCAB.local_class_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.soil_type = Slot(uri=MIXS['0000332'], name="soil_type", curie=MIXS.curie('0000332'),
                   model_uri=MIXS.VOCAB.soil_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.soil_type_meth = Slot(uri=MIXS['0000334'], name="soil_type_meth", curie=MIXS.curie('0000334'),
                   model_uri=MIXS.VOCAB.soil_type_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.slope_gradient = Slot(uri=MIXS['0000646'], name="slope_gradient", curie=MIXS.curie('0000646'),
                   model_uri=MIXS.VOCAB.slope_gradient, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.slope_aspect = Slot(uri=MIXS['0000647'], name="slope_aspect", curie=MIXS.curie('0000647'),
                   model_uri=MIXS.VOCAB.slope_aspect, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.profile_position = Slot(uri=MIXS['0001084'], name="profile_position", curie=MIXS.curie('0001084'),
                   model_uri=MIXS.VOCAB.profile_position, domain=None, range=Optional[str],
                   pattern=re.compile(r'[summit|shoulder|backslope|footslope|toeslope]'))

slots.drainage_class = Slot(uri=MIXS['0001085'], name="drainage_class", curie=MIXS.curie('0001085'),
                   model_uri=MIXS.VOCAB.drainage_class, domain=None, range=Optional[str],
                   pattern=re.compile(r'[very poorly|poorly|somewhat poorly|moderately well|well|excessively drained]'))

slots.texture = Slot(uri=MIXS['0000335'], name="texture", curie=MIXS.curie('0000335'),
                   model_uri=MIXS.VOCAB.texture, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.texture_meth = Slot(uri=MIXS['0000336'], name="texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=MIXS.VOCAB.texture_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.ph_meth = Slot(uri=MIXS['0001106'], name="ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=MIXS.VOCAB.ph_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.tot_org_c_meth = Slot(uri=MIXS['0000337'], name="tot_org_c_meth", curie=MIXS.curie('0000337'),
                   model_uri=MIXS.VOCAB.tot_org_c_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.tot_nitro_content_meth = Slot(uri=MIXS['0000338'], name="tot_nitro_content_meth", curie=MIXS.curie('0000338'),
                   model_uri=MIXS.VOCAB.tot_nitro_content_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.microbial_biomass = Slot(uri=MIXS['0000650'], name="microbial_biomass", curie=MIXS.curie('0000650'),
                   model_uri=MIXS.VOCAB.microbial_biomass, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.microbial_biomass_meth = Slot(uri=MIXS['0000339'], name="microbial_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=MIXS.VOCAB.microbial_biomass_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.link_addit_analys = Slot(uri=MIXS['0000340'], name="link_addit_analys", curie=MIXS.curie('0000340'),
                   model_uri=MIXS.VOCAB.link_addit_analys, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.extreme_salinity = Slot(uri=MIXS['0000651'], name="extreme_salinity", curie=MIXS.curie('0000651'),
                   model_uri=MIXS.VOCAB.extreme_salinity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.salinity_meth = Slot(uri=MIXS['0000341'], name="salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=MIXS.VOCAB.salinity_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.heavy_metals = Slot(uri=MIXS['0000652'], name="heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=MIXS.VOCAB.heavy_metals, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.heavy_metals_meth = Slot(uri=MIXS['0000343'], name="heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=MIXS.VOCAB.heavy_metals_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.al_sat = Slot(uri=MIXS['0000607'], name="al_sat", curie=MIXS.curie('0000607'),
                   model_uri=MIXS.VOCAB.al_sat, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.al_sat_meth = Slot(uri=MIXS['0000324'], name="al_sat_meth", curie=MIXS.curie('0000324'),
                   model_uri=MIXS.VOCAB.al_sat_meth, domain=None, range=Optional[str],
                   pattern=re.compile(r'{PMID}|{DOI}|{URL}'))

slots.biochem_oxygen_dem = Slot(uri=MIXS['0000653'], name="biochem_oxygen_dem", curie=MIXS.curie('0000653'),
                   model_uri=MIXS.VOCAB.biochem_oxygen_dem, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.chem_oxygen_dem = Slot(uri=MIXS['0000656'], name="chem_oxygen_dem", curie=MIXS.curie('0000656'),
                   model_uri=MIXS.VOCAB.chem_oxygen_dem, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.efficiency_percent = Slot(uri=MIXS['0000657'], name="efficiency_percent", curie=MIXS.curie('0000657'),
                   model_uri=MIXS.VOCAB.efficiency_percent, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.emulsions = Slot(uri=MIXS['0000660'], name="emulsions", curie=MIXS.curie('0000660'),
                   model_uri=MIXS.VOCAB.emulsions, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.gaseous_substances = Slot(uri=MIXS['0000661'], name="gaseous_substances", curie=MIXS.curie('0000661'),
                   model_uri=MIXS.VOCAB.gaseous_substances, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.indust_eff_percent = Slot(uri=MIXS['0000662'], name="indust_eff_percent", curie=MIXS.curie('0000662'),
                   model_uri=MIXS.VOCAB.indust_eff_percent, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.inorg_particles = Slot(uri=MIXS['0000664'], name="inorg_particles", curie=MIXS.curie('0000664'),
                   model_uri=MIXS.VOCAB.inorg_particles, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.org_particles = Slot(uri=MIXS['0000665'], name="org_particles", curie=MIXS.curie('0000665'),
                   model_uri=MIXS.VOCAB.org_particles, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.pre_treatment = Slot(uri=MIXS['0000348'], name="pre_treatment", curie=MIXS.curie('0000348'),
                   model_uri=MIXS.VOCAB.pre_treatment, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.primary_treatment = Slot(uri=MIXS['0000349'], name="primary_treatment", curie=MIXS.curie('0000349'),
                   model_uri=MIXS.VOCAB.primary_treatment, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.reactor_type = Slot(uri=MIXS['0000350'], name="reactor_type", curie=MIXS.curie('0000350'),
                   model_uri=MIXS.VOCAB.reactor_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.secondary_treatment = Slot(uri=MIXS['0000351'], name="secondary_treatment", curie=MIXS.curie('0000351'),
                   model_uri=MIXS.VOCAB.secondary_treatment, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.sewage_type = Slot(uri=MIXS['0000215'], name="sewage_type", curie=MIXS.curie('0000215'),
                   model_uri=MIXS.VOCAB.sewage_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.sludge_retent_time = Slot(uri=MIXS['0000669'], name="sludge_retent_time", curie=MIXS.curie('0000669'),
                   model_uri=MIXS.VOCAB.sludge_retent_time, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.soluble_inorg_mat = Slot(uri=MIXS['0000672'], name="soluble_inorg_mat", curie=MIXS.curie('0000672'),
                   model_uri=MIXS.VOCAB.soluble_inorg_mat, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.soluble_org_mat = Slot(uri=MIXS['0000673'], name="soluble_org_mat", curie=MIXS.curie('0000673'),
                   model_uri=MIXS.VOCAB.soluble_org_mat, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.tertiary_treatment = Slot(uri=MIXS['0000352'], name="tertiary_treatment", curie=MIXS.curie('0000352'),
                   model_uri=MIXS.VOCAB.tertiary_treatment, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.tot_phosphate = Slot(uri=MIXS['0000689'], name="tot_phosphate", curie=MIXS.curie('0000689'),
                   model_uri=MIXS.VOCAB.tot_phosphate, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.wastewater_type = Slot(uri=MIXS['0000353'], name="wastewater_type", curie=MIXS.curie('0000353'),
                   model_uri=MIXS.VOCAB.wastewater_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text}'))

slots.atmospheric_data = Slot(uri=MIXS['0001097'], name="atmospheric_data", curie=MIXS.curie('0001097'),
                   model_uri=MIXS.VOCAB.atmospheric_data, domain=None, range=Optional[str],
                   pattern=re.compile(r'{text};{float} {unit}'))

slots.bac_prod = Slot(uri=MIXS['0000683'], name="bac_prod", curie=MIXS.curie('0000683'),
                   model_uri=MIXS.VOCAB.bac_prod, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.bac_resp = Slot(uri=MIXS['0000684'], name="bac_resp", curie=MIXS.curie('0000684'),
                   model_uri=MIXS.VOCAB.bac_resp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.conduc = Slot(uri=MIXS['0000692'], name="conduc", curie=MIXS.curie('0000692'),
                   model_uri=MIXS.VOCAB.conduc, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.diss_inorg_nitro = Slot(uri=MIXS['0000698'], name="diss_inorg_nitro", curie=MIXS.curie('0000698'),
                   model_uri=MIXS.VOCAB.diss_inorg_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.down_par = Slot(uri=MIXS['0000703'], name="down_par", curie=MIXS.curie('0000703'),
                   model_uri=MIXS.VOCAB.down_par, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.fluor = Slot(uri=MIXS['0000704'], name="fluor", curie=MIXS.curie('0000704'),
                   model_uri=MIXS.VOCAB.fluor, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.light_intensity = Slot(uri=MIXS['0000706'], name="light_intensity", curie=MIXS.curie('0000706'),
                   model_uri=MIXS.VOCAB.light_intensity, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.part_org_nitro = Slot(uri=MIXS['0000719'], name="part_org_nitro", curie=MIXS.curie('0000719'),
                   model_uri=MIXS.VOCAB.part_org_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.photon_flux = Slot(uri=MIXS['0000725'], name="photon_flux", curie=MIXS.curie('0000725'),
                   model_uri=MIXS.VOCAB.photon_flux, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.primary_prod = Slot(uri=MIXS['0000728'], name="primary_prod", curie=MIXS.curie('0000728'),
                   model_uri=MIXS.VOCAB.primary_prod, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.size_frac_low = Slot(uri=MIXS['0000735'], name="size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=MIXS.VOCAB.size_frac_low, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.size_frac_up = Slot(uri=MIXS['0000736'], name="size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=MIXS.VOCAB.size_frac_up, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.soluble_react_phosp = Slot(uri=MIXS['0000738'], name="soluble_react_phosp", curie=MIXS.curie('0000738'),
                   model_uri=MIXS.VOCAB.soluble_react_phosp, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.suspend_part_matter = Slot(uri=MIXS['0000741'], name="suspend_part_matter", curie=MIXS.curie('0000741'),
                   model_uri=MIXS.VOCAB.suspend_part_matter, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tot_diss_nitro = Slot(uri=MIXS['0000744'], name="tot_diss_nitro", curie=MIXS.curie('0000744'),
                   model_uri=MIXS.VOCAB.tot_diss_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tot_inorg_nitro = Slot(uri=MIXS['0000745'], name="tot_inorg_nitro", curie=MIXS.curie('0000745'),
                   model_uri=MIXS.VOCAB.tot_inorg_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))

slots.tot_part_carb = Slot(uri=MIXS['0000747'], name="tot_part_carb", curie=MIXS.curie('0000747'),
                   model_uri=MIXS.VOCAB.tot_part_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'{float} {unit}'))
