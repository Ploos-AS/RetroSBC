BUILD_DIR ?= build
TOP := retrocore_top
ECP5_DEVICE := 45k
ECP5_PACKAGE := CABGA381

.PHONY: test synth reva-pnr reva-bitstream clean

test:
	mkdir -p $(BUILD_DIR)
	iverilog -g2012 -o $(BUILD_DIR)/tb $(TOP).v tb_$(TOP).v
	vvp $(BUILD_DIR)/tb

synth:
	mkdir -p $(BUILD_DIR)
	yosys -p 'synth_ecp5 -top $(TOP) -json $(BUILD_DIR)/$(TOP).json' $(TOP).v

reva-pnr: synth
	nextpnr-ecp5 --um5g-$(ECP5_DEVICE) --package $(ECP5_PACKAGE) \
		--json $(BUILD_DIR)/$(TOP).json \
		--textcfg $(BUILD_DIR)/$(TOP).config \
		--lpf-allow-unconstrained \
		--report $(BUILD_DIR)/$(TOP)-pnr.json

reva-bitstream: reva-pnr
	ecppack $(BUILD_DIR)/$(TOP).config $(BUILD_DIR)/$(TOP).bit

# Rev A P&R currently permits unconstrained I/O deliberately. This qualifies
# the selected LFE5UM-45F/BG381 device/package and open-source implementation
# flow, not the final PCB pinout. Remove --lpf-allow-unconstrained when the
# Rev A LPF and FPGA bank/pin allocation are frozen.
clean:
	rm -rf $(BUILD_DIR)
