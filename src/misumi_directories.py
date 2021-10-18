import os

class MisumiDirectories():
    """Create for MISUMI dataset"""
    def __init__(self, misumi_dataset_rootpath):
        self.misumi_dataset_rootpath = misumi_dataset_rootpath
        os.makedirs(self.misumi_dataset_rootpath, exist_ok=True)

        self.inserts_list = [
            'tangless', 'threaded', 'tools_for_tangless', 'tools_for_threaded'
        ]

        self.nuts_list = [
            'cylindrical', 'domed', 'flanged', 'hex', 'high_nuts_and_spacer', 'knurled', 'lock',
            'non-metal', 'rectangular', 'wing', 'weld', 'rivet', 'clinching', 'clip', 'cap', 'washer_based', 'gauge'
        ]

        self.screws_bolts_list = [
            'captive_washer_screws', 'cross_recessed_bolts', 'eye_screws_bolts',
            'fastener_accessories', 'fully-threaded_bolts', 'hex_bolts', 'hex_socket_button_head_cap',
            'hex_socket_flat_head_cap', 'hex_socket_head_cap', 'micro_screws_precise_screws',
            'plastic_ceramic_screws', 'self_tapping_screws', 'set_screws',
            'small_head_bolts', 'space_saving_bolts',
            'strippers_reamers_shoulder_bolts', 'tamper_resistant_screws', 'vented_screws', 'wing_thumb_ornamental'
        ]

        self.shims_list = [
            'rectangular', 'plates', 'rings', 'tape'
        ]

        self.washers_list = [
            'metal', 'non-metal_and_collars', 'urethane_rubber_sponge_felt'
        ]

        self.wiring_components_list = [
                'cable_gland_components',
                'screw_spacer_components',
        ]

        self.lan_and_industrial_network_cables_list = [
            'lan_cable_with_connector', 'lan_network_cable', 'fiber_optic_cable_accessories',
            'lan_cable_connector_accessories', 'network_cable_adapters', 'network_cable_connectors',
            'telephone_cable', 'fiber_optic_cable'
        ]

        self.equipment_specific_cables_list = [
            'ac_servo_motor_cables', 'cordset_accessories', 'io_board_cables', 'image_sonsor_cables',
            'plc_cables', 'relay_terminal_cables', 'sensor_cordsets', 'single_axis_robot_cables',
            'stepper_motor_cables', 'touch_panel_cables', 'solenoid_valve_compatible_cable'
        ]

        self.cordsets_list = [
            'circular', 'coaxial', 'conversion_branching', 'nylon_connector', 'square'
        ]

        self.cable_accessories_list = [
            'cable_accessories', 'conductive_tape', 'electrical_tape'
        ]

        self.cable_bushings_clip_stickers_list = [
            'bushings', 'clips', 'stickers'
        ]

        self.cable_organization_list = [
            'ties', 'tie_mount_accessories'
        ]

        self.cable_gland_list = [
            'components', 'accessories'
        ]

        self.computer_av_cables_list = [
            'audio_video', 'display', 'printer', 'ps2', 'rs232c', 'scsi', 'usb', 'antenna'
        ]

        self.crimp_terminal_components_list = [
            'crimp_terminals', 'crimp_terminal_accessories'
        ]

        self.electrical_conduits_list = [
            'metal', 'metal_conduits_accessories', 'plastic', 'plastic_conduits_accessories'
        ]

        self.electrical_tubing_list = [
            'braided_sleeves', 'cable_sleeving', 'electrical_tubing_accessories', 'general_purpose_tubing',
            'heat_shrink_tubing', 'spiral_wraps'
        ]

        self.electrical_wiring_tools = [
            'cable_tile_tools', 'crimping_idc_tools', 'electrical_wiring_tool_accessories',
            'wire_cutting_tools', 'wiring_connection_screwdrivers', 'wiring_tweezers_wranches',
            'wiring_stripper_tools'
        ]

        self.soldering_supplies_list = [
            'soldering_tools', 'soldering_iron_holders'
        ]

        self.specialized_wiring_tools = [
            'connector_tools', 'specialized_wiring_tool_accessories', 'terminal_removal_tools'
        ]

        self.wire_cable_list = [
            'coaxial', 'coiled', 'control_instrumentation', 'environmentally_friendly', 'flexible_robot', 'hook_up_wires',
            'power', 'ribbon', 'information_communication', 'wire_storage', 'disaster_prevension_alarm', 'lan_network_cable'
        ]

        self.wiring_connectors_list = [
            'circular', 'coaxial', 'connector_accessories', 'connector_adapters', 'connector_caps', 'connector_sets',
            'contacts_cap', 'nylon_connectors', 'rectangular_connectors'
        ]

        self.wire_ducts_cable_raceways_list = [
            'raceways', 'raceways_accessories', 'ducts', 'ducts_accessories'
        ]

    def _create_dir(self, dir_name:str):
        """"
        Create a directory for datasets if not exists.

        Parameters
        ---------------
        dir_name : str
            directory name
        """
        target_dir_path = os.path.join(self.misumi_dataset_rootpath, dir_name)

        if not os.path.exists(target_dir_path):
            os.mkdir(target_dir_path)

    def _create_dirs(self, dir_name_list : list, suffix : str = None):
        """
        Create directories for datasets

        Parameters
        --------------
        dir_name_list : list
            directory name list
        suffix : str, optional
            suffix
        """

        for directory_name in dir_name_list:
            if not suffix == None:
                directory_name = suffix + directory_name

            self._create_dir(directory_name)

    def __call__(self):
        # create directories

        # fasteners
        self._create_dir('hand_tools_for_screws')
        self._create_dir('hair_pins_and_cotter_pins')
        self._create_dir('machine_keys')
        self._create_dir('retaining_rings')
        self._create_dir('screws_plug_hardware')
        self._create_dirs(self.inserts_list, suffix='inserts_')
        self._create_dirs(self.nuts_list, suffix='nuts_')
        self._create_dirs(self.screws_bolts_list, suffix='screwsBolts_')
        self._create_dirs(self.shims_list, suffix='shims_')
        self._create_dirs(self.washers_list, suffix='washers_')

        # wiring components
        self._create_dir('wiringComponents_screw_spacer_components')
        self._create_dirs(self.lan_and_industrial_network_cables_list, suffix='lanAndIndustrial_')
        self._create_dirs(self.equipment_specific_cables_list, suffix='equipmentSpecific_')
        self._create_dirs(self.cordsets_list, suffix='cordsets_')
        self._create_dirs(self.cable_accessories_list, suffix='cableAccessories_')
        self._create_dirs(self.cable_bushings_clip_stickers_list, suffix='cableBushing_')
        self._create_dirs(self.cable_organization_list, suffix='cableOrganization_')
        self._create_dirs(self.cable_gland_list, suffix='cableGland_')
        self._create_dirs(self.computer_av_cables_list, suffix='comAV_')
        self._create_dirs(self.crimp_terminal_components_list, suffix='crimp_')
        self._create_dirs(self.electrical_conduits_list, suffix='electricalConduits_')
        self._create_dirs(self.electrical_tubing_list, suffix='electricalTubing_')
        self._create_dirs(self.electrical_wiring_tools, suffix='electricalWiring_')
        self._create_dirs(self.soldering_supplies_list, suffix='soldering_')
        self._create_dirs(self.specialized_wiring_tools, suffix='specializedWiring_')
        self._create_dirs(self.wire_cable_list, suffix='wireCable_')
        self._create_dirs(self.wiring_connectors_list, suffix='wiringConnectors_')
        self._create_dirs(self.wire_ducts_cable_raceways_list, suffix='wireDucts_')

if __name__ == '__main__':
    misumi_directories = MisumiDirectories("../inputs/misumi_dataset")
    misumi_directories()