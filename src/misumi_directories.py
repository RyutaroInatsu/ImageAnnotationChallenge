import os

class MisumiDirectories():
    """Create for MISUMI dataset"""
    def __init__(self, misumi_dataset_rootpath):
        self.misumi_dataset_rootpath = misumi_dataset_rootpath
        os.makedirs(self.misumi_dataset_rootpath, exist_ok=True)

        self.inserts_subdirectory_list = [
            'tangless', 'threaded', 'tools_for_tangless', 'tools_for_threaded'
        ]

        self.nuts_subdirectory_list = [
            'cylindrical', 'domed', 'flanged', 'hex', 'high_nuts_and_spacer', 'knurled', 'lock',
            'non-metal', 'rectangular', 'wing', 'weld', 'clinching', 'clip', 'cap', 'washer_based', 'gauge'
        ]

        self.screws_bolts_subdirectory_list = [
            'captive_washer_screws', 'cross_recessed_bolts', 'eye_screws_bolts',
            'fastener_accessories', 'fully-threaded_bolts', 'hex_bolts', 'hex_socket_button_head_cap',
            'hex_socket_flat_head_cap', 'hex_socket_head_cap', 'micro_screws_precise_screws',
            'plastic_ceramic_screws', 'self_tapping_screws', 'small_head_bolts', 'space_saving_bolts',
            'strippers_reamers_shoulder_bolts', 'tamper_resistant_screws', 'vented_screws', 'wing_thumb_ornamental'
        ]

        self.shims_subdirectory_list = [
            'rectangular', 'plates', 'rings', 'tape'
        ]

        self.washers_list = [
            'metal', 'non-metal_and_collars'
        ]

        self.wiring_components_directory_list = [
                'lan_and_industrial_network_cables',
                'equipment_specific_cables',
                'cordsets',
                'cable_accessories',
                'cable_gland_components',
                'cable_bushings_clip_and_stickers',
                'cable_organization',
                'computer_av_cables',
                'crimp_terminal_components',
                'electrical_conduits',
                'electrical_tubing',
                'electrical_wiring_tools',
                'screw_spacer_components',
                'soldering_supplies',
                'specialized_wiring_tools',
                'wire_cable',
                'wiring_connectors',
                'wire_ducts_and_cable_raceways'
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
            'wiring stripper tools'
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
            'circular', 'coaxial', 'connector accessories', 'connector adapters', 'connector caps', 'connector sets',
            'contacts cap', 'nylon connectors', 'rectangular connectors'
        ]

        self.wire_ducts_cable_raceways_list = [
            'raceways', 'raceways_accessories', 'ducts', 'ducts_accessories'
        ]

        # Key is directory's name.
        # Value is sub-directories list.
        self.fasteners_directory_dicts = {
            'hand_tools_for_screws' : None,
            'hair_pins_and_cotter_pins' : None,
            'inserts' : self.inserts_subdirectory_list,
            'machine_keys': None,
            'nuts' : self.nuts_subdirectory_list,
            'retaining_rings' : None,
            'screws_and_bolts' : self.screws_bolts_subdirectory_list,
            'screw_plug_hardware' : None,
            'shims' : self.shims_subdirectory_list,
            'washers' :self.washers_list
        }

        # Key is directory's name.
        # Value is sub-directories list.
        self.wiring_directory_dicts = {
            'lan_industrial_network_cables' : self.lan_and_industrial_network_cables_list,
            'equipment_specific_cables' : self.equipment_specific_cables_list,
            'cordsets': self.cordsets_list,
            'cable_accessories': self.cable_accessories_list,
            'cable_gland_components' : None,
            'cable_bushing_clip_stickers': self.cable_bushings_clip_stickers_list,
            'cable_organization': self.cable_organization_list,
            'computer_av_cables': self.computer_av_cables_list,
            'crimp_terminal_components':self.crimp_terminal_components_list,
            'electrical_conduits': self.electrical_conduits_list,
            'electrical_tubing': self.electrical_tubing_list,
            'electrical_wiring_tools':self.electrical_wiring_tools,
            'screw_spacer_components': None,
            'soldering_supplies' : self.soldering_supplies_list,
            'specialized_wiring_tools' : self.specialized_wiring_tools,
            'wire_cable': self.wire_cable_list,
            'wiring_connectors': self.wiring_connectors_list,
            'wire_ducts_cable_raceways': self.wire_ducts_cable_raceways_list
        }

    def _create_dirs(self, parent_dir : str, sub_dir_list : list= None):
        """
        Create directories for datasets

        Parameters
        --------------
        parent_dir : str
        sub_dir_list : list
        """

        target_parent_dir_path = os.path.join(self.misumi_dataset_rootpath, parent_dir)
        os.makedirs(target_parent_dir_path, exist_ok=True)

        if sub_dir_list == None:
            return

        for directory in sub_dir_list:
            target_dir_path = os.path.join(target_parent_dir_path, directory)

            if not os.path.exists(target_dir_path):
                os.mkdir(target_dir_path)

    def __call__(self):
        for parent_dir, sub_dir in self.fasteners_directory_dicts.items():
            self._create_dirs(parent_dir, sub_dir)

        for parent_dir, sub_dir in self.wiring_directory_dicts.items():
            self._create_dirs(parent_dir, sub_dir)

if __name__ == '__main__':
    misumi_directories = MisumiDirectories("../inputs/misumi_dataset")
    misumi_directories()